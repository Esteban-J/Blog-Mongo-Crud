from pymongo import MongoClient
from bson import ObjectId

class ArticleModel:
    def __init__(self):
        self.db = MongoClient('mongodb://localhost:27017/')["blog"]
        self.article_collection = self.db["article"]

    def create_article(self, title, date, text, user_id, comments):

        article_data = {
            "title": title,
            "date": date,
            "text": text,
            "user": user_id,
            "comments": comments
        }

        self.article_collection.insert_one(article_data)
        return True

    def update_article(self, id, title, date, text, user_id, comments):
        if not isinstance(id, ObjectId):
            id = ObjectId(id)
    
        article = self.article_collection.find_one({"_id": id})
        
        if not article:
            return False
        
        title = title if title else article.get("title")
        date = date if date else article.get("date")
        text = text if text else article.get("text")
        user_id = user_id if user_id else article.get("user")
        comments = comments if comments else article.get("comments", [])
    
        self.article_collection.update_one(
            {"_id": id},
            {"$set": {"title": title, "date": date, "text": text, "user": user_id, "comments": comments}}
        )
        return True

    def replace_article(self, id, title=None, date=None, text=None, user_id=None, comments=None):
        if not isinstance(id, ObjectId):
            id = ObjectId(id)
    
        article = self.article_collection.find_one({"_id": id})

        if not article:
            return False
    
        self.article_collection.update_one(
            {"_id": id},
            {"$set": {"title": title, "date": date, "text": text, "user": user_id, "comments": comments}}
        )
        return True

    def delete_article(self, id):

        if not isinstance(id, ObjectId):
            id = ObjectId(id)
    
        result = self.article_collection.delete_one({"_id": id})
        
        return result.deleted_count > 0
    
    def get_user(self):
        return self.article_collection.find()
