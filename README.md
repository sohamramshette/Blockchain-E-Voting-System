# 🗳️ Blockchain E-Voting System

A secure, transparent, and tamper-detectable electronic voting system built using **Blockchain Technology**, **Python Flask**, and **SHA-256 hashing**.

The project demonstrates how blockchain can improve trust, transparency, and integrity in digital voting by storing every vote as an immutable block linked through cryptographic hashes.

---

## 📌 Features

- 👤 Secure Voter Registration
- 🔐 Voter Authentication
- 🗳️ One Vote Per Voter
- ⛓️ Blockchain-based Vote Storage
- 🔒 SHA-256 Hashing
- ⚡ Proof of Work (PoW)
- 📊 Live Election Results
- 🔍 Blockchain Explorer
- 🛡️ Tamper Detection
- ✅ Blockchain Validation
- 🎯 Responsive User Interface

---

# 📷 Screenshots

> Add your project screenshots here.

| Home | Authentication |
|------|---------------|
| ![](screenshots/home.png) | ![](screenshots/auth.png) |

| Voting | Explorer |
|------|---------|
| ![](screenshots/voting.png) | ![](screenshots/explorer.png) |

| Results | Security |
|------|---------|
| ![](screenshots/results.png) | ![](screenshots/security.png) |

---

# 🚀 Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### Blockchain
- SHA-256 Hashing
- Proof of Work
- Previous Hash Linking

### Tools
- VS Code
- Git
- GitHub

---

# 🏗️ System Architecture

```
                User
                  │
                  ▼
      HTML • CSS • JavaScript
                  │
                  ▼
             Flask Backend
                  │
                  ▼
          Voting Blockchain
                  │
      ┌───────────┼───────────┐
      ▼           ▼           ▼
 SHA-256     Proof of Work   Chain Linking
      │
      ▼
 Blockchain Ledger
      │
      ▼
 Results & Explorer
```

---

# ⚙️ How It Works

1. Register a voter.
2. Start the election.
3. Authenticate the voter.
4. Select a candidate.
5. Create a vote block.
6. Generate SHA-256 hash.
7. Mine the block using Proof of Work.
8. Add the block to the blockchain.
9. Update vote tally.
10. Validate blockchain integrity.
11. Display election results.

---

# 🔐 Security Features

- SHA-256 Cryptographic Hashing
- Blockchain Immutability
- Previous Hash Linking
- Double Vote Prevention
- Voter ID Hashing
- Tamper Detection
- Blockchain Validation

---

# 📂 Project Structure

```
Blockchain-EVoting/
│
├── app.py
├── blockchain.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── screenshots/
│
└── README.md
```

---

# 💻 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Blockchain-EVoting-System.git
```

### Move into Project

```bash
cd Blockchain-EVoting-System
```

### Create Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Project

```bash
python app.py
```

Open:

```
http://localhost:5000
```

---

# 🧪 Test Cases

| Test Case | Status |
|-----------|--------|
| Register Voter | ✅ Pass |
| Authenticate Voter | ✅ Pass |
| Cast Vote | ✅ Pass |
| Prevent Duplicate Vote | ✅ Pass |
| Blockchain Explorer | ✅ Pass |
| Tamper Detection | ✅ Pass |
| Blockchain Validation | ✅ Pass |
| Display Results | ✅ Pass |

---

# 🎯 Learning Outcomes

This project demonstrates:

- Blockchain Fundamentals
- SHA-256 Hashing
- Proof of Work
- Blockchain Validation
- Flask Web Development
- REST APIs
- Secure Authentication
- Full Stack Development

---

# 🔮 Future Improvements

- Database Integration
- Aadhaar Authentication
- OTP Verification
- QR Code Login
- Cloud Deployment
- Mobile Application
- Role-Based Access Control
- Advanced Consensus Algorithms
- AI-based Fraud Detection
- Large Scale Election Support

---

# 👨‍💻 Team Members

- **Soham Ramshette**
- **Kunal Patil**
- **Anuj Kadlag**
- **Prashant Girhe**
- **Pratik Wahule**

**Guide:**  
**Prof. Pragati Deole**

Department of Software Engineering  
MIT Academy of Engineering, Pune

---

# 📜 License

This project is developed for educational and academic purposes under the Creative Technologies course at MIT Academy of Engineering.

---

# ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.

It helps others discover the project and motivates further improvements.
