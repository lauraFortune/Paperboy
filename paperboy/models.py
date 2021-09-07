
class News():

    def __init__(self):
        self.categories = []
    
    def create_category(self, category_name):
        category = Category(category_name)
        self.categories.append(category)

        

class Category(): 

    def __init__(self, category_name):
        self.category_name = category_name
        self.articles = []

    def add_article(self, article):
        self.articles.append(article)

    def clear_articles(self):
        self.articles = []


class Article(): 
    def __init__(self, image, url, publish_date, title, description, savedID):
        self.image = image
        self.url = url
        self.publish_date = publish_date
        self.title = title
        self.description = description
        self.savedID = savedID
