from fastapi_crudrouter import SQLAlchemyCRUDRouter

from app.models.potato import Potato, PotatoCreate, PotatoModel

from app.db import get_db

router = SQLAlchemyCRUDRouter(
    schema=Potato,
    create_schema=PotatoCreate,
    db_model=PotatoModel,
    db=get_db,
    prefix="potato",
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
