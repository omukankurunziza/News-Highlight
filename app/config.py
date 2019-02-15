class Config:
    '''
    General configuration parent class
    '''

    NEWS_API_BASE_URL= 'https://newsapi.org/v2/everything?q=bitcoin&from=2019-01-15&sortBy=publishedAt&apiKey=5bf78fd2f43a4de790ccc54004d607fa'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True