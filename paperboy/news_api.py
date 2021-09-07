import requests
from models import *
import backend

# list of all news categories
categories = ['sports', 'business', 'technology']
news = News()

#==========================================================
#           function to get users location
#==========================================================
def get_location():
    URL = "https://ipinfo.io/json"
    r = requests.get(url = URL)
    data = r.json() 
    country = data['country']
    
    return country

#==========================================================
#           function to get news data from news api
#==========================================================
def get_news_data(category_list):

    # define search parameters
    URL = "https://newsapi.org/v2/top-headlines?"
    API_KEY = 'your_api_key' # update your api key here
   
    CATEGORIES = category_list
    COUNTRY = get_location()
    
    articles = []

    for i in range(len(CATEGORIES)): # loop through categories(CATEGORIES) array
        PARAMS = {'category' : CATEGORIES[i], 'country' : COUNTRY, 'apiKey' : API_KEY} # set parameters for each category
        category_json = requests.get(url=URL, params=PARAMS).json()
        articles.append(category_json['articles'])

    return articles

#==========================================================
#           function to create news object
#==========================================================
def create_news_object(category_names,articles_by_category):

    print("Creating News Object")
    global news
    news = News() # instansiate news object

    for i in range(len(articles_by_category)):
    #for category in articles_by_category:
        for name in category_names:
            news.create_category(name)
        for article in articles_by_category[i]:
            news_article = Article(article['urlToImage'], article['url'],article['publishedAt'], article['title'], article['description'], -1)
            news.categories[i].add_article(news_article)

def resetMyNewsCategory():
    global news
    news.categories[3].clear_articles()
    for story in backend.show():
        urlToImage = story[2]
        url = story[3]
        publishedAt = story[4]
        title = story[5]
        description = story[6]
        savedID = story[0]
        print(savedID)

        news_article = Article(urlToImage, url, publishedAt, title, description, savedID)
        news.categories[3].add_article(news_article)

def addMyNewsCategory():
    
    global news
    news.create_category("My News")
    
    for story in backend.show():
        urlToImage = story[2]
        url = story[3]
        publishedAt = story[4]
        title = story[5]
        description = story[6]
        savedID = story[0]
        print(savedID)

        news_article = Article(urlToImage, url, publishedAt, title, description, savedID)
        news.categories[3].add_article(news_article)

def buildNewsObject():
    articles_by_category=get_news_data(categories)
    create_news_object(categories,articles_by_category)
    addMyNewsCategory()
    print("News Initialised")
