from sqlalchemy.orm import mapped_column, Mapped

from sqlalchemy import Float
from sqlalchemy import func
from datetime import datetime

from app.db.database import Base




class EspData(Base):
    __tablename__ = "esp_data"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[datetime] = mapped_column(insert_default=func.now(), nullable=False)
    temp: Mapped[Float] = mapped_column(Float, nullable=False)
    hum: Mapped[Float] = mapped_column(Float, nullable=False)