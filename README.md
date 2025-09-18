🔐 Password Strength Checker & Data Breach Detection
📌 Overview
This project is a password security tool that helps users:
Check the strength of a password (weak, medium, strong) based on multiple security rules.
Verify whether the password has appeared in known data breaches using the HaveIBeenPwned API (k-anonymity model).
It is designed to raise awareness about strong password practices and highlight risks of using compromised credentials.

⚙️ Features
✅ Password strength analysis (length, complexity, entropy).
✅ Real-time feedback (weak/medium/strong).
✅ Data breach check via HIBP API (no plain password is leaked).
✅ Command-line tool (CLI) or Web UI (optional).
✅ Secure handling of user input.

🛠️ Tech Stack
Language: Python 3
Libraries Used:
requests – API calls to HaveIBeenPwned
hashlib – password hashing (SHA-1)
re – regex for password rules
argparse / tkinter – CLI or simple GUI (if implemented)

🚀 Installation
Clone the repo:
git clone https://github.com/sibubehera097-byte/Password-Strength-Checker-and-Data-Breaches.git
cd Password-Strength-Checker-and-Data-Breaches

▶️ Usage
Check Password Strength Only
python password_checker.py --password "My@StrongPass123"

Check for Data Breach
python password_checker.py --password "My@StrongPass123" --check-breach

📊 Example Output
Password Strength: Strong ✅
Your password has NOT been found in any known data breaches. 🎉

Password Strength: Weak ❌
⚠️ Warning: This password has been seen 542,123 times in known data breaches!
