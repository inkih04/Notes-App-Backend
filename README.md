# 🗒️ Notes App Backend

This is the **Notes App backend**, developed with Django and Django REST Framework. It provides a RESTful API for managing notes and notebooks, with authentication via Google OAuth2 and JWT.

> 🔗 **Production API:**  
> https://notes-app-backend-37a9.onrender.com/

---

## 🚀 Main Features

- 📝 **Notes** CRUD operations
- 📁 **Notebooks** CRUD operations
- 🔐 **Authentication** with Google OAuth 2.0
- 🔄 **JWT** (access and refresh tokens)
- 🌐 **CORS** configured for frontend access (Vercel)
- ⚙️ API ready to connect with React/Vite frontend

---

## 📦 Requirements

- Python 3.10+
- pip
- Git
- SQLite (included by default with Python)

---

## 🛠️ Local Installation

To run the project locally, you can use the included script:

```bash
./run-localDev.sh
```

This script:

✅ Creates a virtual environment (venv/)

📦 Installs dependencies from requirements.txt

🔄 Applies migrations automatically

🚀 Starts the server at: http://127.0.0.1:8000/

## 🔐 Environment Variables

Create a `.env` file in the project root using python-decouple.

Minimal configuration example:

```bash
SECRET_KEY=your_secret_key
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
EMAIL_HOST_PASSWORD=your_app_password
FRONTEND_URL=http://localhost:3000
```

## 📁 Project Structure

```bash
notes_backend/
├── notes/                  # Main app (notes, notebooks, profiles)
├── notes_backend/          # Django project configuration
├── run-localDev.sh         # Local development script
├── requirements.txt
└── manage.py
```

## 🌐 Production Deployment

This backend is deployed on Render, using Gunicorn as the WSGI server.
Currently uses SQLite database, but is prepared to easily migrate to PostgreSQL.

## 🔗 Useful Links

🧠 Frontend Repository (React + Vite): Notes-App-Frontend

⚙️ Production Backend: Render - API Link

📦 API Docs: pending implementation

## 📌 Notes

- Active development is done on the `dev` branch
- For pull requests and collaborations, please base your changes on the `dev` branch

## 🧑‍💻 Author

Developed by @inkih04