from fastapi import Query
from typing import Annotated

import datetime as dt
from app.schemas.file import FileType



async def get_beg_date(beg_date : Annotated[dt.date, Query(default_factory=dt.date.today)]) -> dt.date:
    return beg_date

async def get_end_date(end_date : Annotated[dt.date, Query(default_factory=dt.date.today)]):
    return end_date

async def get_file_type(type: Annotated[FileType, Query(...)]):
    return type.value 