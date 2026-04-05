# 🤖 Lindoom AI — IT Support Chatbot

An AI-powered customer support chatbot for Lindoom IT Services.
Built with Python, FastAPI, Google Gemini, Docker, and deployed on Railway + Netlify.

## 🌍 Live Demo
- **Frontend:** https://lindoom-ai.netlify.app
- **Backend:** https://lindoom-ai-production.up.railway.app

## ✨ Features
- Real-time AI chat powered by Google Gemini
- Professional IT support persona (Lindo)
- Responsive chat widget embedded in company website
- RESTful API backend
- Dockerized for consistent deployment
- Auto-deploys on every GitHub push

## 🛠️ Tech Stack
| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, FastAPI |
| AI | Google Gemini 2.5 Flash |
| Container | Docker |
| Backend Host | Railway |
| Frontend Host | Netlify |
| Version Control | GitHub |

## 🚀 Run Locally
1. Clone the repo
2. Create a `.env` file in `/backend` with your `GEMINI_API_KEY`
3. Run `docker-compose up`
4. Open `frontend/index.html`

## 📁 Project Structure
lindoom-ai/
├── backend/
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   └── index.html
└── docker-compose.yml