from fastapi import APIRouter
from fastapi import Depends

import datetime as dt

from app.service import esp as db
from app.handlers import esp as handler

router = APIRouter()

@router.get('/check')
async def get_data():
    return await db.get_ten_data()


@router.get('/from_date', 
            description='Получение данных в заданный промежуток дат')
async def get_data_between_date(
                             beg_date: dt.date = Depends(handler.get_beg_date),
                             end_date: dt.date = Depends(handler.get_end_date),
                            ):
    return await db.get_date_date(beg_date, end_date)

@router.get('/out_file')
async def get_data_file_between_date(
                             beg_date: dt.date = Depends(handler.get_beg_date),
                             end_date: dt.date = Depends(handler.get_end_date),
                             file_type: str = Depends(handler.get_file_type)):
    json_data = await db.get_date_date(beg_date, end_date)
