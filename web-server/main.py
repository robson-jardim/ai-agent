from fastapi import FastAPI
from router import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def home():
    return {"status": "AI Agent is running"}

@app.get("/test")
def test():
    return {"status": "The router test works!"}
