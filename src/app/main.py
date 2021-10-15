from fastapi import FastAPI

from app.api import routers
from app.api.models import Base
from app.db import engine
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:8081",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers.router, prefix="/api", tags=["api"])
