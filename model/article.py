from pymongo import MongoClient

class ArticleModel:
    def __init__(self):
        self.db = MongoClient('mongodb://localhost:27017/')["blog"]
        self.articles_collection = self.db["articles"]

    def create_article(self, title, content):
        if title and content:
            self.articles_collection.insert_one({"title": title, "content": content})
            return True
        return False

    def get_articles(self):
        return self.articles_collection.find()

    def update_article(self, article_id, new_content):
        self.articles_collection.update_one({"_id": article_id}, {"$set": {"content": new_content}})
        return True

    def delete_article(self, article_id):
        self.articles_collection.delete_one({"_id": article_id})
        return True
