from fastapi import FastAPI, Header
from pydantic import BaseModel
from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class MessageInput(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "AI Agent is running"}

@app.post("/webhook")
async def webhook(payload: MessageInput, x_source: str = Header(default="unknown")):
    user_input = payload.message
    print(f"[{x_source}] Message received: {user_input}")

    # 🔥 GPT-4/3.5 call
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Or "gpt-3.5-turbo" for lower cost
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
