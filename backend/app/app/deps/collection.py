import httpx

from app.core.config import settings 

from  .news import NEWS_API_MAPPING
from .reddit import REDDIT_API_MAPPING
from .sample import API_MAPPING
from .cache import timed_lru_cache


# Register your API in this API-COLLECTION
API_COLLECTIONS = [
    REDDIT_API_MAPPING,
    NEWS_API_MAPPING,
    #API_MAPPING

]


# === Search Endpoint ===
# Call 'Search' endpoint of all registered APIs
@timed_lru_cache(settings.LRU_CACHE_DURATION)
def get_news(limit):
    """
    This function will get top news from all registered APIs (in API_COLLECTIONS).
    :param limit: Integer number to limit number of responses from each API.
    :return: Return aggregated news results.
    """
    response = []
    for api in API_COLLECTIONS:
        result = httpx.get(api["listing_url"].format(limit=limit),
                              headers={'User-agent': 'bot v1'}).json()
        if result:
            response += api["parser"](result)
    return response


#
# Call 'Search' endpoint of all registered APIs
@timed_lru_cache(settings.LRU_CACHE_DURATION)
def search_news(query, limit):
    """
     This function will get search results for given QUERY from all registered APIs (in API_COLLECTION).

    :param query: Search Query.
    :param limit: Integer number to limit number of responses from each API.
    :return: Return aggregated news results.
    """
    response = []
    for api in API_COLLECTIONS:
        result = httpx.get(api["search_url"].format(query=query, limit=limit),
                              headers={'User-agent': 'bot v1'}).json()
        if result:
            response += api["parser"](result)
    return response
