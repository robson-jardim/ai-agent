# 🤖 AI Agent Router for Workout Coaching

This project is a FastAPI-based AI agent that integrates with OpenAI's GPT API to provide smart, personalized workout conversations. It's designed for personal trainers, fitness coaches, and digital apps that want to automate high-quality fitness messaging.

---

## 🧠 Features

- Accepts messages from any source (Instagram, SMS, etc.)
- Routes the input to OpenAI's GPT for personalized response
- Easy to extend with database, scheduling, or user profiles
- Deployable in minutes using Render

---

## 📁 Project Structure

```
ai-agent-router/
├── main.py             # FastAPI app
├── requirements.txt    # Python dependencies
├── render.yaml         # Deployment instructions for Render
└── .env                # Local API keys (not committed)
```

---

## 🚀 Deploy Session (Render)

This section explains how to deploy the AI Agent to a live production environment using [Render.com](https://render.com).

### ✅ Prerequisites

- A [Render](https://render.com) account
- A GitHub repository containing this project
- An OpenAI API key

---

### 📄 Step-by-Step Deployment

#### 1. **Push the Project to GitHub**

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ai-agent-router.git
git push -u origin main
```

---

#### 2. **Prepare `render.yaml`**

```yaml
services:
  - type: web
    name: ai-agent-router
    env: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "uvicorn main:app --host 0.0.0.0 --port $PORT"
    plan: free
    envVars:
      - key: OPENAI_API_KEY
        sync: false
```

---

#### 3. **Deploy on Render**

- Go to [https://render.com](https://render.com)
- Click **"New" → "Web Service"**
- Connect your GitHub repo
- Render will detect your `render.yaml` and auto-deploy
- In **Environment → Add Environment Variable**, create:
  - `OPENAI_API_KEY` = `your-real-api-key`

---

#### 4. **Test Your Live API**

```bash
curl -X POST https://your-app-name.onrender.com/webhook \
  -H "Content-Type: application/json" \
  -H "x-source: test" \
  -d '{"message": "give me a workout"}'
```

You should receive a JSON reply from OpenAI through your FastAPI app.

---

### ✅ Done!

You now have a production-ready AI agent running on FastAPI + OpenAI, publicly accessible via HTTPS.
