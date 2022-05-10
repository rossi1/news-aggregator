from ast import Str
import secrets
from typing import List, Union, Optional

from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):
    API_STR: str = "/api"
    SECRET_KEY: Optional[str] = secrets.token_urlsafe(32)
    
    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl

    DNS: AnyHttpUrl
    ENVIRONMENT: str
    
    NEWS_API_KEY: str
    LRU_CACHE_DURATION: int

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str


    class Config:
        case_sensitive = True


settings = Settings()
