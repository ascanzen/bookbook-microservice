from fastapi import FastAPI
from app.api.potato import router as potato_router
from app.api.daily_account import router as daily_account_router
from app.db import create_db_and_tables

app = FastAPI()

app.include_router(potato_router)
app.include_router(daily_account_router)


@app.on_event("startup")
def on_startup():
    # Not needed if you setup a migration system like Alembic
    return create_db_and_tables()
