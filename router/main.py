from fastapi import FastAPI, Request, Header
from pydantic import BaseModel

app = FastAPI()

class MessageInput(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "AI Agent is running"}

@app.post("/webhook")
def webhook(payload: MessageInput, x_source: str = Header(default="unknown")):
    print(f"[{x_source}] Message received: {payload.message}")

    if "workout" in payload.message.lower():
        return {"reply": "Let’s get started with your workout 💪"}
    return {"reply": "Hello, world!"}


