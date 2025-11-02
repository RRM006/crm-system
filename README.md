# CRM System - Web & Android App

## 📋 Project Overview
Full-stack CRM system with web interface and Android mobile app.

## 🛠️ Tech Stack
- **Frontend:** React.js
- **Backend:** Django (Python)
- **Mobile:** Android (Kotlin)
- **Database:** Supabase (PostgreSQL)

## 👥 User Roles
1. Admin
2. Sales Executive
3. Customer Support Agent
4. Manager/Supervisor
5. Customer (External)

## 📂 Project Structure
```
crm-system/
├── frontend/          # React web app
├── backend/           # Django REST API
├── mobile/            # Android app
└── docs/              # Documentation
```

## 🚀 Setup Status
- [x] Project structure created
- [x] Backend API (Django + DRF + JWT)
- [x] Local database (SQLite) migrations OK
- [x] Supabase PostgreSQL config ready (toggle via env)
- [x] Auth endpoints (register/login JWT)
- [x] Core models (Customers, Leads, Tasks, Complaints)
- [x] Frontend scaffold (React + Vite + Bootstrap)
- [ ] Android app scaffold (Kotlin)

## 📝 Development Progress
**Current Phase:** Phase 1 – Core CRM
**Last Updated:** 02/11/25

---

## 🧪 Quick Start (Beginner friendly)

1) Backend – run API

Create a backend/.env from the example:

```
copy backend\.env.example backend\.env
```

Keep USE_SQLITE=true for local practice. Then:

```
cd backend
python -m venv venv
venv\Scripts\pip install -r requirements.txt
venv\Scripts\python manage.py migrate
venv\Scripts\python manage.py runserver
```

2) Frontend – run web app

```
cd frontend
copy .env.example .env
npm install
npm run dev
```

Open http://localhost:5173 and login/register; API is at http://localhost:8000.

3) Switch to Supabase (shared online DB)

Edit backend/.env:

- set `USE_SQLITE=false`
- fill `DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT`

Then re-run on backend:

```
venv\Scripts\python manage.py migrate
venv\Scripts\python manage.py runserver
```

4) Build APK (later)

Open the mobile/ project in Android Studio, build an APK from Build > Build Bundle(s)/APK(s).

---

## 🔐 Auth Endpoints
- POST /api/auth/register/  {email, password, role, username, first_name, last_name}
- POST /api/auth/token/     {email, password} -> {access, refresh}
- GET  /api/auth/me/        Authorization: Bearer <access>

## 📦 Core API
- Customers: /api/customers/
- Leads: /api/leads/
- Tasks: /api/tasks/
- Complaints: /api/complaints/

All require JWT except `/api/health/`.

---

## 🌐 Deployment (free tiers)

- Database: Supabase (PostgreSQL) – already provisioned by you.
- Backend: Render.com or Railway.app (free tier). Set environment variables from backend/.env.example and set `USE_SQLITE=false`.
- Frontend: Netlify or Vercel (free). Set `VITE_API_BASE_URL` to your deployed backend URL + `/api`.

---

## 📱 Mobile (Kotlin)
We provide a minimal Retrofit-based sample to login and fetch customers. See `mobile/README.md` for step-by-step instructions to create an APK.

## 🔗 Links
- Backend API: (will add after deployment)
- Frontend Web: (will add after deployment)
- Documentation: See /docs folder

---
**Course:** CSE327
**Developer:** []