import uuid

from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    phone_number: str
    pass


class UserCreate(schemas.BaseUserCreate):
    phone_number: str
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass
