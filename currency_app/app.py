from fastapi import FastAPI, APIRouter

from .routers import info, currency


app = FastAPI()

app.include_router(info.router)
app.include_router(currency.router)
