from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app import database
from app import api, views


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

database.Base.metadata.create_all(bind=database.engine)

app.include_router(api.router)
app.include_router(views.router)
