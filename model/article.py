from pymongo import MongoClient
from bson import ObjectId

class ArticleModel:
    def __init__(self):
        self.db = MongoClient('mongodb://localhost:27017/')["blog"]
        self.article_collection = self.db["article"]

    def create_article(self, title, date, text, user_id, comments, tags, categories):

        article_data = {
            "title": title,
            "date": date,
            "text": text,
            "user": user_id,
            "comments": comments,
            "tags": tags,
            "categories": categories
        }

        self.article_collection.insert_one(article_data)
        return True

    def update_article(self, id, title, date, text, user_id, comments, tags, categories):
        if not isinstance(id, ObjectId):
            id = ObjectId(id)
    
        article = self.article_collection.find_one({"_id": id})
        
        if not article:
            return False
        
        update_data = {}
        if title:
            update_data["title"] = title
        if date:
            update_data["date"] = date
        if text:
            update_data["text"] = text
        if user_id:
            update_data["user"] = user_id
        if comments:
            update_data["comments"] = comments
        if tags:
            update_data["tags"] = tags
        if categories:
            update_data["categories"] = categories
        if update_data:
            self.article_collection.update_one({"_id": id}, {"$set": update_data})
            return False
        return True

    def replace_article(self, id, title, date, text, user_id, comments, tags, categories):
        if not isinstance(id, ObjectId):
            id = ObjectId(id)
    
        article = self.article_collection.find_one({"_id": id})

        if not article:
            return False
    
        self.article_collection.update_one(
            {"_id": id},
            {"$set": {"title": title, "date": date, "text": text, "user": user_id, "comments": comments, "tags": tags, "categories": categories}}
        )
        return True

    def delete_article(self, id):

        if not isinstance(id, ObjectId):
            id = ObjectId(id)
    
        result = self.article_collection.delete_one({"_id": id})
        
        return result.deleted_count > 0
    
    def get_articles(self):
        return list(self.article_collection.find())
