
from app.core.config import settings

NEWS_API_KEY = settings.NEWS_API_KEY

def newsapi_parser(data):
    """
    :param results: JSON Object
    :return: List of dictionaries
            [
                {
                    "title": "title of the news",
                    "link": "original link of the news source",
                    "source":"your-api-name"
                },
            ...
            ]
    """
    response = []
    for child in data["articles"]:
        response.append({
            "title": child["title"],
            "link": child["url"],
            "source": "newsapi"
        })
    return response


NEWS_API_MAPPING = {
    "api_name": "newsapi",
    "parser": newsapi_parser,
    "listing_url": 'http://newsapi.org/v2/top-headlines?category=general&pageSize={limit}&page=1&' +
                   'apiKey={api_key}'.format(api_key=NEWS_API_KEY),
    "search_url": 'http://newsapi.org/v2/everything?q={query}&pageSize={limit}&page=1&' +
                  'apiKey={api_key}'.format(api_key=NEWS_API_KEY)
}
