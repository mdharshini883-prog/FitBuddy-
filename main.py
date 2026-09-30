from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from app.routes import router

app = FastAPI(title="FitBuddy - AI Fitness Plan Generator")

templates = Jinja2Templates(directory="templates")

app.include_router(router)