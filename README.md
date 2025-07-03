# Secure-file-Sharing
# 🔐 Secure File Sharing System (Flask Version)

This is a secure file-sharing backend built using **Flask**, **SQLite**, and **JWT authentication**. It supports two types of users:

- 🛠 **Ops User** – can upload `.pptx`, `.docx`, and `.xlsx` files
- 👤 **Client User** – can sign up, verify email, login, list files, and download securely via encrypted URL

---

## 📦 Features

- Role-based access (Ops / Client)
- File upload (restricted types for Ops only)
- Email verification via tokenized URL
- JWT-secured login & download
- Secure download URLs, valid for Client users only
- SQLite-based storage
- Simple REST APIs

---

## 🛠 Tech Stack

- Python 3.x
- Flask
- SQLite
- JWT (via `pyjwt`)
- Werkzeug (for secure file handling)

---

## 🚀 Getting Started

### 🔧 Installation

```bash
git clone https://github.com/yourusername/flask-file-sharing.git
cd flask-file-sharing
python -m venv venv
venv\Scripts\activate        # On Windows
pip install -r requirements.txt
