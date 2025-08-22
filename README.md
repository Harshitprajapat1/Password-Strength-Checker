# 🔐 Password Strength Checker (Streamlit App)

This project is a **Password Strength Checker** built using **Python** and **Streamlit**.  
It evaluates the strength of a password, provides improvement suggestions, and estimates the time it would take for an attacker to crack the password.

---

## ✨ Features
- ✅ Checks **minimum length** (at least 8 characters required)  
- ✅ Evaluates **password strength** based on:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters  
- ✅ Provides **suggestions** to improve weak passwords  
- ✅ Estimates **cracking time** using brute-force calculation  
- ✅ Visualizes strength with **progress bar**  
- ✅ Displays **rating with emoji** (Very Weak → Very Strong)  

---

## 🖥️ Demo Screenshot
*(Add your screenshot here after running the app)*  
Example:

<img width="1919" height="1020" alt="Screenshot 2025-08-21 173730" src="https://github.com/user-attachments/assets/601f4b9a-84c7-4dc1-90b0-0d5e24754d89" />


---

## 🚀 Installation & Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/password-strength-checker.git
   cd password-strength-checker

python -m venv venv
source venv/bin/activate    # On Mac/Linux
venv\Scripts\activate       # On Windows

streamlit run password_checker_app.py

