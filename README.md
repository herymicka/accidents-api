
# 🚀 Accidents Prediction API (MLOps Project)

Production-ready Machine Learning API for road accident prediction, deployed with BentoML and Render.

---

## 🌐 Live API

👉 https://accidents-api.onrender.com

---

## ⚙️ Tech Stack

- Python
- Scikit-learn
- BentoML
- Docker
- Render (Cloud Deployment)
- JWT Authentication

---

## 📌 Features

- ✅ Machine Learning model (Random Forest)
- ✅ REST API with BentoML
- ✅ Secure authentication with JWT
- ✅ Automated deployment (Docker + Render)
- ✅ MLOps pipeline (training → serving → deployment)

---

## 🔐 Authentication

### Login

```bash
curl -X POST "https://accidents-api.onrender.com/login" \
  -H "Content-Type: application/json" \
  -d '{
    "request": {
      "credentials": {
        "username": "user123",
        "password": "password123"
      }
    }
  }'
