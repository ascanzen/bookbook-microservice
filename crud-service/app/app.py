from fastapi import FastAPI
from app.api.potato import router as potato_router
from app.api.daily_account import router as daily_account_router

app = FastAPI()
app.include_router(potato_router)
app.include_router(daily_account_router)
