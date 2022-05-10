
def reddit_parser(data):
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
    for child in data["data"]["children"]:
        response.append({
            "title": child["data"]["title"],
            "link": child["data"]["url"],
            "source": "reddit"
        })
    return response


REDDIT_API_MAPPING = {
    "api_name": "reddit",
    "parser": reddit_parser,
    "listing_url": ('https://www.reddit.com/r/news/top.json?'
                    'limit={limit}'),
    "search_url": ('https://www.reddit.com/r/news/search.json?'
                   'q={query}&'
                   'limit={limit}')
}
