def sample_parser(data):
    """
    :param results: JSON Object
    :return: List of dictionaries
            [
                {
                    "title": "title of the news",
                    "link": "original link of the news source",
                    "source":"api-name"
                },
            ...
            ]
    """
    # Change the Body accordingly...
    response = []
    for child in data["data"]["children"]:
        response.append({
            "title": child["data"]["title"],
            "link": child["data"]["url"],
            "source": "api-name" #include the api source
        })
    return response


API_MAPPING = {
    "api_name": "api-name", # Include the api name
    "parser": sample_parser,
    "listing_url": "link-to-your-api-listing?limit={limit}",
    "search_url": "link-to-your-api-search-endpoint?q={query}&limit={limit}"
}
