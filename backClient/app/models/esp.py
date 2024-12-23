from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Float, func
from datetime import datetime


class Base(DeclarativeBase):
    pass

class EspData(Base):
    __tablename__ = "esp_data"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[datetime] = mapped_column(insert_default=func.now(), nullable=False)
    temp: Mapped[Float] = mapped_column(Float, nullable=False)
    hum: Mapped[Float] = mapped_column(Float, nullable=False)

    def to_dict(self):
        return {
            'temp': self.temp,
            'hum': self.hum,
            'date': self.date.strftime('%d-%m-%Y')
        }