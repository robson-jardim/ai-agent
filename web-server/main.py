from fastapi import FastAPI, Header
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import openai

from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

class MessageInput(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "AI Agent is running"}

@app.get("/test")
def test():
    return {"status": "The router test works!"}

@app.post("/webhook")
async def webhook(payload: MessageInput, x_source: str = Header(default="unknown")):
    user_input = payload.message
    print(f"[{x_source}] Message received: {user_input}")

    # ✅ New GPT call using openai>=1.0.0
    try:
        response = client.chat.completions.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a helpful fitness assistant. Respond like a coach, motivating and guiding users."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=200
        )
        ai_reply = response.choices[0].message.content.strip()
    except Exception as e:
        print("Error:", e)
        ai_reply = "Sorry, I had trouble generating a response. Please try again."

    return {"reply": ai_reply}
