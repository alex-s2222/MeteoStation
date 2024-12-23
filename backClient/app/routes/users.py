from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import FileResponse
from fastapi import BackgroundTasks

import datetime as dt

import os

from app.db import esp as db
from app.handlers import esp as handler
from app.service.converter import Converter


router = APIRouter()

def remove_file(path: str):
    os.remove(path)

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
                             file_type: str = Depends(handler.get_file_type),
                             ):
    json_data = await db.get_date_date(beg_date, end_date)
    
    current_dir = os.getcwd() + '/output'
    file_name = f"data.{file_type}"
    file_path = os.path.join(current_dir, file_name)

    Converter.save_and_get_file_path(json_data, file_type, file_path)
    
    # background_tasks.add_task(remove_file, file_path)
    return FileResponse(path=file_path, filename=file_name, media_type='multipart/form-data')