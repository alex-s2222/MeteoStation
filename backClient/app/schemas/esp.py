from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class getDataByDate(BaseModel):
    beg_date: Optional[datetime] 
    end_date: Optional[datetime]