from fastapi import FastAPI
from api import routes

app = FastAPI(title="Flight Search API")
app.include_router(routes.router)