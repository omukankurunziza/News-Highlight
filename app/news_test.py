import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News("fox-news","Fox News","Beto O'Rourke says he 'absolutely' supports destroying existing walls on southern border - Fox News","Former Texas Democratic Rep. Beto O'Rourke on Thursday that he would \"absolutely\" support tearing down existing barriers along the southern border with Mexico, in a full-throated embrace of open-borders rhetoric that has left conservatives wondering where oth…",'https://media2.foxnews.com/BrightCove/694940094001/2019/01/17/694940094001_5990490713001_5990491506001-vs.jpg',"2019-02-15T02:55:21Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()