from typing import  List

from sentry_sdk import capture_exception

from fastapi import APIRouter, HTTPException

from app.schemas import APIResponse
from app.deps import search_news, get_news

router = APIRouter()

@router.get("/", response_model =List[APIResponse])
async def list_news(q: str = None, limit: int = 10) -> List[APIResponse]:
    """
    This single endpoint will server getting Top-Listings and Search functionality
    for news aggregation APIs.
    """
    try:
        if q is not None:
            # call search endpoint
            result = search_news(q, limit)
        else:
            # call news listing endpoint
            result = get_news(limit)

        return result
    except Exception as e:
        print(str(e))
        capture_exception(e)
        raise HTTPException(status_code=422, detail="Unable to process request at this time")

     
