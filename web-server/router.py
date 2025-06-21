from fastapi import APIRouter, Header
from models import MessageInput
from intent_handler import detect_intent, handle_intent

router = APIRouter()

@router.post("/webhook")
async def webhook(payload: MessageInput, x_source: str = Header(default="unknown")):
    user_input = payload.message
    print(f"[{x_source}] Message received: {user_input}")
    intent = detect_intent(user_input)
    response = handle_intent(intent, user_input)
    return {"reply": response}
