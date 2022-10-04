import datetime
from fastapi import Depends, FastAPI
from fastapi.encoders import jsonable_encoder

from app.db import User, create_db_and_tables
from app.users import (
    current_active_user,
)
from .schemas.daily_account import DailyAccountCommit
from model.daily_account_table import DailyAccount

app = FastAPI(openapi_url="/api/v1/users/openapi.json", docs_url="/api/v1/users/docs")


@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


# @app.post("/commit-daily-account")
# async def commit_daily_account(record: DailyAccountCommit):
#     # TODO change tablename table tag
#     TableT = DailyAccount.create_son_table("user1", location="beijing", groupid=3)
#     json = jsonable_encoder(record)

#     res = TableT.select().where(DailyAccount.id == record.id).one()
#     # 如果已经提交
#     if res:
#         # TODO 比较update time
#         if record.updateTime > res.updateTime:
#             # update
#             # TODO
#             pass
#     else:
#         # 新加
#         m = TableT(
#             **json,
#             ts=datetime.datetime.now(),
#         )
#         m.save()


@app.post("/pull/{model}")
async def pull():
    return {"message": f"Hello"}


@app.on_event("startup")
async def on_startup():
    # Not needed if you setup a migration system like Alembic
    await create_db_and_tables()
