from fastapi import FastAPI

from app.routes import users

def create_app():
    app = FastAPI(
        title='ClientMeteoStation'
    )
    return app 

app = create_app()

app.include_router(users.router, prefix='', tags=['Users'])