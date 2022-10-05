from fastapi import FastAPI
from app.api.potato import router as potato_router

app = FastAPI()
app.include_router(potato_router)
