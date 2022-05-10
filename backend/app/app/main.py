import os

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
import sentry_sdk

from app.api.api import api_router
from app.core.config import settings


sentry_sdk.init(
    dsn=settings.DNS,  
    environment=settings.ENVIRONMENT
)

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_STR}/openapi.json"
)


try:
    app.add_middleware(SentryAsgiMiddleware)
except Exception:
    # pass silently if the Sentry integration failed, You can also log the errors here
    pass

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_STR)



