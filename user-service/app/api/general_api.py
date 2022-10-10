from datetime import datetime, timedelta
from typing import List, TypeVar
from fastapi import APIRouter, Depends
from fastapi_crudrouter import SQLAlchemyCRUDRouter


from app.db import get_db, User
from app.users import current_active_user

TModel = TypeVar("TModel")

from pydantic_sqlalchemy import sqlalchemy_to_pydantic


def get_router(model: TModel) -> APIRouter:

    PydanticSchema = sqlalchemy_to_pydantic(model)

    def camel_to_snake(s):
        return (
            "".join(["_" + c.lower() if c.isupper() else c for c in s])
            .lstrip("_")
            .replace("'>", "")
        )

    router = SQLAlchemyCRUDRouter(
        schema=PydanticSchema,
        create_schema=PydanticSchema,
        update_schema=PydanticSchema,
        db_model=model,
        db=get_db,
        prefix=f"/api/v1/{camel_to_snake(str(model).split('.')[-1])}",
    )

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
        db_models: List[PydanticSchema] = (
            db.query(router.db_model)
            .filter(
                router.db_model.user == str(user.id),
                router.db_model.syncTime > syncTime,
            )
            .order_by(getattr(router.db_model, router._pk))
            .all()
        )
        return db_models

    return router
