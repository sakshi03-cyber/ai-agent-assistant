from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="AI Agent API")

app.include_router(router)