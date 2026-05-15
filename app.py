"""
app.py — Flask Web Application for Blockchain E-Voting System
Run with:  python app.py
Then open: http://localhost:5000
"""

from flask import Flask, request, jsonify, render_template
from blockchain import VotingBlockchain
import hashlib

import os
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))

# ── Global State ─────────────────────────────────────────────
bc = VotingBlockchain()

CANDIDATES = [
    {"id": "A", "name": "Alice Johnson",  "party": "Progress Party", "color": "#3b82f6"},
    {"id": "B", "name": "Bob Williams",   "party": "Liberty Union",  "color": "#ef4444"},
    {"id": "C", "name": "Carol Martinez", "party": "Green Future",   "color": "#22c55e"},
    {"id": "D", "name": "David Chen",     "party": "United Front",   "color": "#f59e0b"},
]

CANDIDATE_MAP = {c["id"]: c for c in CANDIDATES}

# ─────────────────────────────────────────────────────────────
#  FRONTEND
# ─────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html", candidates=CANDIDATES)


# ─────────────────────────────────────────────────────────────
#  API — STATUS
# ─────────────────────────────────────────────────────────────

@app.route("/api/status")
def status():
    tally = bc.get_tally()
    valid, msg = bc.is_valid()
    results = []
    total = bc.total_votes
    for c in CANDIDATES:
        votes = tally.get(c["id"], 0)
        results.append({
            **c,
            "votes": votes,
            "percent": round(votes / total * 100, 1) if total else 0,
        })
    return jsonify({
        "phase": bc.phase,
        "block_count": len(bc.chain),
        "total_votes": total,
        "registered_voters": len(bc.voters),
        "chain_valid": valid,
        "validity_message": msg,
        "candidates": results,
    })


# ─────────────────────────────────────────────────────────────
#  API — VOTER REGISTRATION
# ─────────────────────────────────────────────────────────────

@app.route("/api/register", methods=["POST"])
def register():
    body = request.get_json()
    voter_id = body.get("voter_id", "").strip()
    name     = body.get("name", "").strip()
    ok, msg  = bc.register_voter(voter_id, name)
    return jsonify({"success": ok, "message": msg,
                    "voters": [{"id": vid, "name": vname}
                               for vid, vname in bc.voters.items()]})


@app.route("/api/voters")
def get_voters():
    return jsonify([{"id": vid, "name": vname} for vid, vname in bc.voters.items()])


# ─────────────────────────────────────────────────────────────
#  API — VOTING
# ─────────────────────────────────────────────────────────────

@app.route("/api/authenticate", methods=["POST"])
def authenticate():
    body     = request.get_json()
    voter_id = body.get("voter_id", "").strip()
    if voter_id not in bc.voters:
        return jsonify({"success": False, "message": "Voter ID not found."})
    if bc.phase != "voting":
        return jsonify({"success": False,
                        "message": "Voting is not active yet." if bc.phase == "registration"
                        else "Election has ended."})
    already = voter_id in bc.voted
    return jsonify({
        "success": True,
        "name": bc.voters[voter_id],
        "already_voted": already,
        "anon_id": hashlib.sha256((voter_id + "🔒_secure_salt_2026").encode()).hexdigest()[:16],
    })


@app.route("/api/vote", methods=["POST"])
def vote():
    body         = request.get_json()
    voter_id     = body.get("voter_id", "").strip()
    candidate_id = body.get("candidate_id", "").strip()

    if candidate_id not in CANDIDATE_MAP:
        return jsonify({"success": False, "message": "Invalid candidate."})

    ok, result = bc.cast_vote(voter_id, candidate_id)
    if not ok:
        return jsonify({"success": False, "message": result})

    return jsonify({
        "success": True,
        "message": "Vote recorded on blockchain!",
        "block": result.to_dict(),
    })


# ─────────────────────────────────────────────────────────────
#  API — ADMIN / PHASE CONTROL
# ─────────────────────────────────────────────────────────────

@app.route("/api/admin/start", methods=["POST"])
def admin_start():
    ok, msg = bc.start_voting()
    return jsonify({"success": ok, "message": msg, "phase": bc.phase})


@app.route("/api/admin/end", methods=["POST"])
def admin_end():
    ok, msg = bc.end_election()
    return jsonify({"success": ok, "message": msg, "phase": bc.phase})


# ─────────────────────────────────────────────────────────────
#  API — BLOCKCHAIN EXPLORER
# ─────────────────────────────────────────────────────────────

@app.route("/api/chain")
def chain():
    blocks = []
    for b in bc.chain:
        d = b.to_dict()
        if d["data"].get("type") == "vote":
            cid = d["data"].get("candidate_id")
            d["candidate_info"] = CANDIDATE_MAP.get(cid)
        blocks.append(d)
    return jsonify(blocks)


@app.route("/api/chain/validate")
def validate():
    valid, msg = bc.is_valid()
    return jsonify({"valid": valid, "message": msg, "blocks": len(bc.chain)})


# ─────────────────────────────────────────────────────────────
#  API — TAMPER DEMO (educational only)
# ─────────────────────────────────────────────────────────────

@app.route("/api/tamper", methods=["POST"])
def tamper():
    """Modify block #1 data to demonstrate tamper detection."""
    if len(bc.chain) < 2:
        return jsonify({"success": False, "message": "Need at least 2 blocks to demonstrate."})
    # Corrupt the hash of block 1 without recomputing
    bc.chain[1].hash = "TAMPERED_" + bc.chain[1].hash[9:]
    valid, msg = bc.is_valid()
    return jsonify({"success": True, "message": "Block #1 tampered!", "chain_valid": valid, "detail": msg})


@app.route("/api/restore", methods=["POST"])
def restore():
    """Restore tampered block by recomputing its hash."""
    if len(bc.chain) < 2:
        return jsonify({"success": False, "message": "Nothing to restore."})
    # Restore correct hash
    bc.chain[1].hash = bc.chain[1].calculate_hash()
    # Re-link subsequent blocks
    for i in range(2, len(bc.chain)):
        bc.chain[i].previous_hash = bc.chain[i - 1].hash
        bc.chain[i].hash = bc.chain[i].calculate_hash()
    valid, msg = bc.is_valid()
    return jsonify({"success": True, "message": "Blockchain restored!", "chain_valid": valid, "detail": msg})


# ─────────────────────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("\n" + "═" * 52)
    print("  🗳️  Blockchain E-Voting System")
    print("  🌐  http://localhost:5000")
    print("═" * 52 + "\n")
    app.run(debug=True, port=5000)
