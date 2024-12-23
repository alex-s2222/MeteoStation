from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from app.db.database import async_session
from app.models.esp_data import EspData


async def set_data_from_esp(temp: float, hum: float) -> None:
    try:
        async with async_session() as conn:
            async with conn.begin():
                new_data = EspData(temp=temp, hum=hum)
                conn.add(new_data)
                await conn.commit()
        return "Успех"
    except SQLAlchemyError as e:
        return "Неа"


async def get_ten_data(limit: int = 10):
    esp_data = None
    async with async_session() as conn:
        stm = select(EspData).order_by(EspData.id.desc()).limit(limit)
        result = await conn.execute(stm)
        esp_data = result.scalars().all()
    
    result = [data.__dict__ for data in esp_data]
    return result