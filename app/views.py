from flask import render_template,request,redirect,url_for
from app import app
from .request import get_news,search_news, get_articles
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting general news        
    general_news = get_news('general')
    # business_news = get_news('business')
    # technology_news = get_news('technology')
    # print(general_news)
    title = 'NewsHighlight - Welcome to The best News Review Website Online'
    # search_news = request.args.get('news_query')

    # if search_news:
    #     return redirect(url_for('search',news_name=search_news))
    # else:
    return render_template('index.html', title = title,general = general_news)
@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    news = get_articles(id)
    title = f'{news.title}'
    return render_template('news.html',title = title,news=news)
@app.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search articles
    '''
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search articles for {news_name}'
    return render_template('search.html',news = searched_news)