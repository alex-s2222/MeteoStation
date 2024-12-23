from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.service.esp import set_data_from_esp, get_ten_data
from app.schemas.esp import SensorData



def create_app():
    app = FastAPI(
        title='MeteoStation'
    )
    return app


app = create_app()


@app.get("/")
async def read_root():
    return await get_ten_data()


@app.post("/")
async def read_data(data: SensorData):
    result = await set_data_from_esp(data.temperature, data.humidity)
    return JSONResponse(content={"message": result}, status_code=200)
    
