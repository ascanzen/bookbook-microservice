from fastapi import Depends, FastAPI

from app.db import User, create_db_and_tables
from app.schemas import UserCreate, UserRead, UserUpdate
from app.users import (
    SECRET,
    auth_backend,
    current_active_user,
    fastapi_users,
    # google_oauth_client,
)

from app.models.daily_account import DailyAccount
from fastapi_crudrouter import MemoryCRUDRouter as CRUDRouter


app = FastAPI(openapi_url="/api/v1/users/openapi.json", docs_url="/api/v1/users/docs")

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
# app.include_router(
#     fastapi_users.get_oauth_router(google_oauth_client, auth_backend, SECRET),
#     prefix="/auth/google",
#     tags=["auth"],
# )


@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


from typing import Any, Callable, List, Type, cast, Optional, Union


router = CRUDRouter(schema=DailyAccount)


# @router.get("")
# def overloaded_get_all():
#     return "My overloaded route that returns all the items"


@router.put("/{item_id}")
def overloaded_update(item_id: int, model: router.update_schema):
    try:
        res = router._get_one()(item_id)
        if res.updateTime < model.updateTime:
            return router._update(item_id, model)
        else:
            return router._get_one()(item_id)
    except:
        # not exist
        return router._create()(model)


app.include_router(router)


@app.on_event("startup")
async def on_startup():
    # Not needed if you setup a migration system like Alembic
    await create_db_and_tables()
