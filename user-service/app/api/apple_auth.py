from datetime import datetime, timedelta
from typing import List
from fastapi import APIRouter, Depends, Response, HTTPException, status, Query
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from loguru import logger
from app.users import get_user_manager

# from app.models.daily_account import DailyAccount, DailyAccountCreate, DailyAccountModel

from app.db import get_db, User
from app.schemas import UserCreate
from app.users import (
    SECRET,
    auth_backend,
    current_active_user,
    fastapi_users,
    # google_oauth_client,
)
from app.utility.apple import AppleClient
from app.users import auth_backend, get_jwt_strategy
from fastapi_users.router.common import ErrorCode, ErrorModel

router = APIRouter(
    prefix="/api/v1/apple",
)


@router.post("/login")
async def login(
    response: Response,
    apple_token: str = Query(
        "eyJraWQiOiJZdXlYb1kiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL2FwcGxlaWQuYXBwbGUuY29tIiwiYXVkIjoiY29tLnllc2ZlZWxpbmcuZml0bmVzc1oiLCJleHAiOjE2MTYyMjM2NjQsImlhdCI6MTYxNjEzNzI2NCwic3ViIjoiMDAwNDAyLjY5ZWMyOGU4M2NiMTQ3NDdhNzE1N2U4M2FlZDAzYmJmLjA2NTQiLCJjX2hhc2giOiI2dE5jb2pLdUFyTU90ZlpQWWtQVjJBIiwiZW1haWwiOiJtNTdreGJiZzk5QHByaXZhdGVyZWxheS5hcHBsZWlkLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjoidHJ1ZSIsImlzX3ByaXZhdGVfZW1haWwiOiJ0cnVlIiwiYXV0aF90aW1lIjoxNjE2MTM3MjY0LCJub25jZV9zdXBwb3J0ZWQiOnRydWV9.IOnYN0WnfiZHDSF2gwFbnKQqWvqxnNxvlsEsUkH88MdBNoxbPQFISq8rLIE4LZIMehOiYvSpdkLZIVTVa2kXhFob38BGXw9JCVxFfjgBXDZou7Dma9HZ_WGybJvTLp2Iz50HKVG_N3EsyjBNr6TUp9DBZrwYeeXalzWKH-_Taj11LvRWYYqoV6CCQ8D-UYI_MqNOlVd5WVtZhoQQKVB0HMK0iZFK_gc1jmUD6IqCtIAs5GRwrPQ_lw6--Ja_dx7rofyH3c4OjhTwZz4Hm6NxOIoMAaAsHzR0aEb6A1qHt944DOTCotrS5Xi13VU2yOFUb7IilhoC0beXROsjLToYlg",
        title="jwt",
        description="apple jwt token: m57kxbbg99@privaterelay.appleid.com",
    ),
    db=Depends(get_db),
    strategy=Depends(get_jwt_strategy),
    user_manager=Depends(get_user_manager),
):

    try:
        client = AppleClient()
        email = client.get_verified_email(apple_token)
        user = db.query(User).filter(User.email == email).one_or_none()
        if user:
            # 成功认证
            return await auth_backend.login(strategy, user, response)
        else:
            # 注册
            db_model: User = User(
                email=email,
                hashed_password="xxxxxxxx",
                is_active=True,
                is_verified=True,
                phone_number="00000000000",
            )
            db.add(db_model)
            db.commit()
            user = db.query(User).filter(User.email == email).one()
            return await auth_backend.login(strategy, user, response)
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ErrorCode.LOGIN_USER_NOT_VERIFIED,
        )
