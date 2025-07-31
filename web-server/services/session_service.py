import redis
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User

load_dotenv()

# Initialize Redis
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    db=0,
    ssl=True,
    decode_responses=True
)

def get_user_session(user_id: str) -> dict:
    session_key = f"session:{user_id}"
    session_data = redis_client.hgetall(session_key)

    if session_data:
        return session_data

    # Fallback to PostgreSQL
    db: Session = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    db.close()

    if user:
        session_data = {
            "name": user.name,
            "goal": user.goal,
            "onboarded": str(user.onboarded)
        }
        redis_client.hset(session_key, mapping=session_data)
        redis_client.expire(session_key, 3600)
        return session_data

    return {}

def save_user_session(user_id: str, session_data: dict):
    session_key = f"session:{user_id}"
    redis_client.hset(session_key, mapping=session_data)
    redis_client.expire(session_key, 3600)

    # Optional: update PostgreSQL too
    db: Session = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()

    if user:
        user.name = session_data.get("name", user.name)
        user.goal = session_data.get("goal", user.goal)
        user.onboarded = session_data.get("onboarded", "false").lower() == "true"
    else:
        user = User(
            id=user_id,
            name=session_data.get("name", "Guest"),
            goal=session_data.get("goal", "not_set"),
            onboarded=session_data.get("onboarded", "false").lower() == "true"
        )
        db.add(user)

    db.commit()
    db.close()
