from fastapi import Depends, FastAPI

from app.db import User, create_db_and_tables
from app.users import (
    current_active_user,
)

app = FastAPI(openapi_url="/api/v1/users/openapi.json", docs_url="/api/v1/users/docs")


@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


@app.post("/commit/{model}")
async def commit():
    return {"message": f"Hello"}


@app.post("/pull/{model}")
async def pull():
    return {"message": f"Hello"}


@app.on_event("startup")
async def on_startup():
    # Not needed if you setup a migration system like Alembic
    await create_db_and_tables()
