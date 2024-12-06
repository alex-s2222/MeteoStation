from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

import datetime


class SensorData(BaseModel):
    temperature: float
    humidity: float


def create_app():

    app = FastAPI(
        title='MeteoStation',
        debug=True
    )
    return app


app = create_app()

global_data = {1: {
                       "temp": 23.40 ,
                       "hum": 41.00
                       }
        }


@app.get("/")
def read_root():
    return global_data


@app.post("/")
def read_data(data: SensorData):
    timestamp = datetime.datetime.now().timestamp()
    
    global_data[timestamp] = {
                            "temp": data.temperature,
                            "hum": data.humidity
                            }
    return JSONResponse(content={"message": "Данные успешно приняты"}, status_code=200)
    
