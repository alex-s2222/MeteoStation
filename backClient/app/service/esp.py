from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from datetime import datetime

from app.db.database import async_session
from app.models.esp import EspData




async def get_ten_data(limit: int = 10):
    esp_data = None
    async with async_session() as conn:
        stm = select(EspData).order_by(EspData.id.desc()).limit(limit)
        result = await conn.execute(stm)
        esp_data = result.scalars().all()
    
    result = [data.__dict__ for data in esp_data]
    return result


async def get_date_date(beg_date: datetime, end_date: datetime):
    esp_data = None 

    async with async_session() as conn:
        stm = select(EspData).filter(EspData.date.between(beg_date, end_date))
        result = await conn.execute(stm)
        esp_data = result.scalars().all()

    result = [data.__dict__ for data in esp_data]
    return result


