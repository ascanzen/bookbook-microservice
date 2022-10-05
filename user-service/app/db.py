from typing import AsyncGenerator, List

from fastapi import Depends
from fastapi_users.db import (
    SQLAlchemyBaseOAuthAccountTableUUID,
    SQLAlchemyBaseUserTableUUID,
    SQLAlchemyUserDatabase,
)
from sqlalchemy import String, create_engine, Column
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from app.settings import config_settings

Base: DeclarativeMeta = declarative_base()


class OAuthAccount(SQLAlchemyBaseOAuthAccountTableUUID, Base):
    pass


class User(SQLAlchemyBaseUserTableUUID, Base):
    phone_number: str = Column(String, default="", nullable=False)
    oauth_accounts: List[OAuthAccount] = relationship("OAuthAccount", lazy="joined")


engine = create_async_engine(config_settings.database_url)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User, OAuthAccount)


engine_sync = create_engine(
    config_settings.database_url_sync, connect_args={"check_same_thread": False}
)
Session_sync = sessionmaker(autocommit=False, autoflush=False, bind=engine_sync)


def get_db():
    session = Session_sync()
    try:
        yield session
        session.commit()
    finally:
        session.close()
