from fastapi import APIRouter, Header
from models import Base, User
from database import SessionLocal, engine
from session_service import get_user_session, save_user_session
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.post("/webhook")
async def webhook(message: dict, x_user_id: str = Header(default="guest")):
    user_id = x_user_id
    session_data = get_user_session(user_id)

    if not session_data.get("onboarded"):
        session_data["onboarded"] = "true"
        save_user_session(user_id, session_data)
        return {"reply": "Welcome! What's your fitness goal?", "user_id": user_id}

    return {
        "reply": f"Hi {session_data.get('name', 'Guest')}! How can I assist you today?",
        "user_id": user_id
    }
