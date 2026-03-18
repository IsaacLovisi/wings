from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.api import api_router
from app.core.database import engine, Base
from app.models import event, ticket
import time
import logging

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Retry logic for database connection on startup
    retries = 5
    while retries > 0:
        try:
            Base.metadata.create_all(bind=engine)
            logger.info("Database connection successful and tables created.")
            break
        except Exception as e:
            retries -= 1
            logger.warning(f"Database connection failed, retrying... {retries} attempts left.")
            time.sleep(2)
    yield

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {"status": "ok", "mensagem": f"{settings.PROJECT_NAME} rodando perfeito!"}