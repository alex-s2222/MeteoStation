from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from sqlalchemy.ext.asyncio import  AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, declared_attr

from app.config.db import DB

DATABASE_URL = DB.get_db_url()

engine = create_async_engine(DATABASE_URL)

class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"