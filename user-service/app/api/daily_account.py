from app.models.daily_account import DailyAccount, DailyAccountCreate, DailyAccountModel

from .general_api import get_router

router = get_router(
    DailyAccount, DailyAccountCreate, DailyAccountCreate, DailyAccountModel
)
