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


another version    ......


# 🔐 Secure File Sharing System – FastAPI

This project implements a secure file-sharing backend using **FastAPI**, **SQLAlchemy**, **JWT authentication**, and a relational database (SQLite or PostgreSQL). It supports two types of users:

- 🛠 **Ops User** – can login and upload `.pptx`, `.docx`, and `.xlsx` files
- 👤 **Client User** – can sign up, verify email, login, list all files, and download via secure encrypted URL

---

## 📦 Features

- JWT authentication for secure access
- Role-based access control
- Upload only valid file types
- Email verification using tokenized links
- Encrypted download links (valid for client users only)
- SQLite for development (easy to migrate to PostgreSQL for production)
- Modular code structure with FastAPI routing

---

## 🛠 Tech Stack

- Python 3.8+
- FastAPI
- SQLAlchemy
- SQLite / PostgreSQL
- JWT (`python-jose`)
- Password hashing (`passlib`)
- Pydantic for schema validation

---

## 📁 Project Structure


```

backend-intern-test/
├── app/
│   ├── **init**.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   ├── utils.py
│   └── routes/
│       ├── ops\_user.py
│       └── client\_user.py
├── uploads/
├── requirements.txt
├── .env
├── .gitignore
├── postman\_collection.json
└── README.md

````

---

## 🚀 Getting Started

### 🔧 Installation

```bash
git clone https://github.com/yourusername/backend-intern-test.git
cd backend-intern-test
python -m venv venv
venv\Scripts\activate   # On Windows
pip install -r requirements.txt
````

---

### ⚙️ Configuration

Create a `.env` file in the root:

```env
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=supersecretkey
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

### ▶️ Running the Server

```bash
uvicorn app.main:app --reload
```

API docs available at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧪 API Endpoints

### 🔹 Ops User

| Method | Endpoint      | Description                      |
| ------ | ------------- | -------------------------------- |
| POST   | `/ops/login`  | Login as Ops user                |
| POST   | `/ops/upload` | Upload `.pptx/.docx/.xlsx` files |

### 🔹 Client User

| Method | Endpoint                     | Description                   |
| ------ | ---------------------------- | ----------------------------- |
| POST   | `/client/signup`             | Register a new client user    |
| GET    | `/client/verify-email`       | Verify email via token        |
| POST   | `/client/login`              | Login as client               |
| GET    | `/client/files`              | List all uploaded files       |
| GET    | `/client/download/{file_id}` | Download a file (client only) |

> Download URL returns a JWT-protected link unique to each file.

---

## 🧪 Testing

Use the built-in Swagger docs or import `postman_collection.json` into Postman to test all endpoints.

---

## 🚀 Deployment Tips

* Use Uvicorn or Gunicorn in production
* Replace SQLite with PostgreSQL
* Store uploaded files in AWS S3 or another secure storage
* Secure secrets using environment variables

---

## 📄 License

MIT License — open for use and modification
