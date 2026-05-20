from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="SmartMarket API")
app.include_router(router)
