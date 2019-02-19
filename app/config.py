class Config:
    '''
    General configuration parent class
    '''
    NEWS_SOURCE_API_BASE_URL= 'https://newsapi.org/v2/sources?apiKey=2ac4f1aeb1c84eba9807e140b299880e'
    NEWS_API_BASE_URL= 'https://newsapi.org/v2/everything?q=bitcoin&from=2019-01-15&sortBy=publishedAt&apiKey=2ac4f1aeb1c84eba9807e140b299880e'



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