class Source:
    '''Source class to define source objects'''

    def __init__(self,id,name,description):
        self.id = id
        self.name = name
        self.description = description
        
class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,name,author,title,description, urlToImage,publishedAt):
        self.id =id
        self.name = name
        self.author = author
        self.title= title
        self.description= description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt