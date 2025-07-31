from fastapi import FastAPI

# import routers
from routers.webhook import router as webhook_router

app = FastAPI()
app.include_router(webhook_router)

@app.get("/")
def home():
    return {"status": "AI Agent is running"}

