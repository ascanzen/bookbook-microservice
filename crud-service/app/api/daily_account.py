from typing import List
from fastapi_crudrouter import SQLAlchemyCRUDRouter

from app.models.daily_account import DailyAccount, DailyAccountCreate, DailyAccountModel

from app.db import get_db

router = SQLAlchemyCRUDRouter(
    schema=DailyAccount,
    create_schema=DailyAccountCreate,
    db_model=DailyAccountModel,
    db=get_db,
    prefix="daily_account",
)


# @router.get("")
# def overloaded_get_all():
#     return "My overloaded route that returns all the items"


def insert_or_update_imp(item_id: int, model: router.update_schema):
    try:
        res = router._get_one()(item_id)
        if res.updateTime < model.updateTime:
            return router._update(item_id, model)
        else:
            return router._get_one()(item_id)
    except:
        # not exist
        return router._create()(model)


@router.put("/commit/{item_id}")
def insert_or_update(item_id: int, model: router.update_schema):
    return insert_or_update_imp(item_id, model)


@router.put("/commits")
def insert_or_update(models: List[router.update_schema]):
    for model in models:
        item_id = model.id
        insert_or_update_imp(item_id, model)
    return "ok"
