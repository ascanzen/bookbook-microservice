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
