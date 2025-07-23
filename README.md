# 🗒️ Notes App Backend

Este es el **backend de la aplicación Notes App**, desarrollado con Django y Django REST Framework. Ofrece una API RESTful para gestionar notas y notebooks, con autenticación vía Google OAuth2 y JWT.

> 🔗 **API en producción:**  
> https://notes-app-backend-37a9.onrender.com/

---

## 🚀 Características principales

- 📝 CRUD de **notas**
- 📁 CRUD de **notebooks**
- 🔐 **Autenticación** con Google OAuth 2.0
- 🔄 **JWT** (access y refresh tokens)
- 🌐 **CORS** configurado para acceso desde frontend (Vercel)
- ⚙️ API lista para conectar con frontend en React/Vite

---

## 📦 Requisitos

- Python 3.10+
- pip
- Git
- SQLite (incluido por defecto con Python)

---

## 🛠️ Instalación local

Para correr el proyecto localmente, puedes usar el script incluido:

```bash
./run-localDev.sh
```
Este script:

✅ Crea un entorno virtual (venv/)

📦 Instala dependencias desde requirements.txt

🔄 Aplica migraciones automáticamente

🚀 Inicia el servidor en: http://127.0.0.1:8000/

🔐 Variables de entorno
Creamos un archivo .env en la raíz del proyecto usando python-decouple.

Ejemplo de configuración mínima:

env
```bash
SECRET_KEY=tu_clave_secreta
GOOGLE_CLIENT_ID=tu_google_client_id
GOOGLE_CLIENT_SECRET=tu_google_client_secret
EMAIL_HOST_PASSWORD=tu_contraseña_de_aplicacion
FRONTEND_URL=http://localhost:3000
```
## 📁 Estructura del proyecto
```bash
notes_backend/
├── notes/                  # App principal (notas, notebooks, perfiles)
├── notes_backend/          # Configuración del proyecto Django
├── run-localDev.sh         # Script de desarrollo local
├── requirements.txt
└── manage.py
```

## 🌐 Despliegue en producción
Este backend está desplegado en Render, usando Gunicorn como servidor WSGI.
Actualmente se utiliza una base de datos SQLite, pero está preparado para migrar fácilmente a PostgreSQL.

🔗 Enlaces útiles
🧠 Repositorio Frontend (React + Vite): Notes-App-Frontend

⚙️ Backend en producción: Render - API Link

📦 API Docs: pendiente de implementación

📌 Notas
El desarrollo activo se realiza en la rama dev

Para pull requests y colaboraciones, por favor, basa tus cambios en la rama dev.

🧑‍💻 Autor
Desarrollado por @inkih04








