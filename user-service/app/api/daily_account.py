from datetime import datetime, timedelta
from typing import List
from fastapi import Depends
from fastapi_crudrouter import SQLAlchemyCRUDRouter

from app.models.daily_account import DailyAccount, DailyAccountCreate, DailyAccountModel

from app.db import get_db, User
from app.users import (
    SECRET,
    auth_backend,
    current_active_user,
    fastapi_users,
    # google_oauth_client,
)

router = SQLAlchemyCRUDRouter(
    schema=DailyAccount,
    create_schema=DailyAccountCreate,
    update_schema=DailyAccountCreate,
    db_model=DailyAccountModel,
    db=get_db,
    prefix="/api/v1/daily_account",
)


# @router.get("")
# def overloaded_get_all():
#     return "My overloaded route that returns all the items"


def insert_or_update_imp(item_id: int, model: router.update_schema):
    db = next(get_db())
    try:
        res = router._get_one()(item_id, db=db)
        if res.updateTime < model.updateTime:
            return router._update(item_id, model, db=db)
        else:
            return router._get_one()(item_id, db=db)
    except:
        # not exist
        return router._create()(model, db=db)


@router.put("/commit/{item_id}")
def insert_or_update(
    item_id: int,
    model: router.update_schema,
    user: User = Depends(current_active_user),
):
    model.syncTime = int(datetime.timestamp(datetime.now()))
    model.user = str(user.id)
    return insert_or_update_imp(item_id, model)


@router.post("/commits")
def insert_or_update(
    models: List[router.update_schema],
    user: User = Depends(current_active_user),
):
    syncTime = int(datetime.timestamp(datetime.now()))
    for model in models:
        item_id = model.id
        model.user = str(user.id)
        model.syncTime = syncTime
        insert_or_update_imp(item_id, model)
    return "ok"


@router.post("/pulls")
def pull(
    syncTime: int = int(datetime.timestamp(datetime.now() - timedelta(days=7))),
    db=Depends(get_db),
    user: User = Depends(current_active_user),
):
    db_models: List[DailyAccount] = (
        db.query(router.db_model)
        .filter(
            router.db_model.user == str(user.id), router.db_model.syncTime > syncTime
        )
        .order_by(getattr(router.db_model, router._pk))
        .all()
    )
    return db_models
