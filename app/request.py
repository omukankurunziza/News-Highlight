from app import app
import urllib.request,json
from .models import news
News = news.News
Source = news.Source
# Getting api key
api_key = app.config['NEWS_API_KEY']
# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]
news_url = app.config["NEWS_SOURCE_API_BASE_URL"]

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = news_url
    print(get_news_url)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_articles = None

        if get_news_response['sources']:
            news_articles_list = get_news_response['sources']
            news_articles = process_sources(news_articles_list)


    return news_articles
def get_articles(id):
    get_news_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            name= news_details_response.get('name')
            author = news_details_response.get('author')
            title = news_details_response.get('title')
            description = news_details_response.get('description')
            urlToImage = news_details_response.get('urlToImage') 
            publishedAt = news_details_response.get('publishedAt')

            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)

    return movie_object
def process_sources(news_list):
    '''
    Function  that processes the news articles and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_articles: A list of news objects
    '''
    news_sources = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        news_object = Source(id,name,description)
        news_sources.append(news_object)

    return news_sources
def search_news(news_name):
    search_news_url = 'https://newsapi.org/v2/{}?q=bitcoin&from=2019-01-15&sortBy=publishedAt&apiKey={}'.format(api_key,news_name)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_articles = None

        if search_news_response['articles']:
            search_news_list = search_news_response['articles']
            search_news_articles = process_articles(search_news_list)


    return search_news_articles
    pass