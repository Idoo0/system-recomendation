from fastapi import FastAPI
from routes.update import update
app = FastAPI()
app.include_router(update)
