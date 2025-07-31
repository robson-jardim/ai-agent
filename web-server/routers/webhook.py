from fastapi import APIRouter, Header


router = APIRouter(prefix="/webhook", tags=["webhook"])

@router.post("/")
async def webhook(message: dict, x_user_id: str = Header(default="guest")):
    return {"status": "received", "user": x_user_id}

@router.post("/start_session")
async def start_sessionn():
    return {"status": "received"}

