import logging.config
from os import path

from fastapi import FastAPI
from src.api.user import router as UserApiRouter
from src.util.exceptions import exception_handler

# TODO: complete logging configuration
log_file_path = path.join(path.dirname(__file__), "logging.conf")
logging.config.fileConfig(log_file_path, disable_existing_loggers=False)

app = FastAPI(
    title="FastAPI Demo",
    description="FastAPI Demo",
    version="0.1",
)

app.middleware("http")(exception_handler)

app.include_router(UserApiRouter, prefix="/api/v1/user", tags=["user"])
