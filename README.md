# 🚀 Accidents Prediction API (MLOps Project)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python">
  <img src="https://img.shields.io/badge/ML-Scikit--Learn-orange">
  <img src="https://img.shields.io/badge/API-BentoML-green">
  <img src="https://img.shields.io/badge/Deployment-Render-purple">
  <img src="https://img.shields.io/badge/Docker-Enabled-blue?logo=docker">
  <img src="https://img.shields.io/badge/Status-Production-success">
</p>

---

## 🌐 Live API

👉 https://accidents-api.onrender.com

---

## 🎯 Project Overview

Production-ready Machine Learning API that predicts road accident risk using a Random Forest model.

This project demonstrates a full **MLOps pipeline**:

➡️ Data → Training → Model → API → Deployment

---

## ⚙️ Tech Stack

- 🐍 Python
- 🤖 Scikit-learn (Random Forest)
- 🚀 BentoML (model serving)
- 🐳 Docker (containerization)
- ☁️ Render (cloud deployment)
- 🔐 JWT Authentication

---

## 🧠 Features

- ✅ Machine Learning model (Random Forest)
- ✅ REST API (BentoML)
- ✅ Secure authentication (JWT)
- ✅ Automated deployment (Docker + Render)
- ✅ Model training at startup
- ✅ Production-ready API

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
