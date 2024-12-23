from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from sqlalchemy.ext.asyncio import  AsyncAttrs, AsyncSession
from sqlalchemy.orm import DeclarativeBase, declared_attr

from app.config.db import DB

DATABASE_URL = DB.get_db_url()

engine = create_async_engine(DATABASE_URL)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}"