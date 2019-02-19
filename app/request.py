from app import app
import urllib.request,json
from .models import news
News = news.News
# Getting api key
api_key = app.config['NEWS_API_KEY']
# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]
def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_articles = None

        if get_news_response['articles']:
            news_articles_list = get_news_response['articles']
            news_articles = process_articles(news_articles_list)


    return news_articles
def get_news(id):
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
def process_articles(news_list):
    '''
    Function  that processes the news articles and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_articles: A list of news objects
    '''
    news_articles = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        urlToImage= news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')

        if urlToImage:
            news_object = News(id,name,author,title,description, urlToImage,publishedAt)
            news_articles.append(news_object)

    return news_articles
    pass