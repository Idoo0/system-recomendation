import flag
from fastapi import FastAPI
from routes.update import update
from routes.recomendation import recomendation

app = FastAPI()

app.include_router(update)
app.include_router(recomendation)