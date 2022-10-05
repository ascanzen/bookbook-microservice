from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine("sqlite:///./app.db", connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base: DeclarativeMeta = declarative_base()


def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()


def create_db_and_tables():
    Base.metadata.create_all(bind=engine)
