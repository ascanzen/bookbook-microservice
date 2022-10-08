from app.models.daily_account import DailyAccountModel as model

from .general_api import get_router

router = get_router(model)
