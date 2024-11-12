from pymongo import MongoClient
from bson import ObjectId

class CategoryModel:
    def __init__(self):
        self.db = MongoClient('mongodb://localhost:27017/')["blog"]
        self.category_collection = self.db["category"]

    def create_category(self, name, url, articles):
        category_data = {
            "name": name,
            "url": url,
            "articles": articles
        }
        self.category_collection.insert_one(category_data)
        return True

    def update_category(self, id, name=None, url=None, articles=None):
        if not isinstance(id, ObjectId):
            id = ObjectId(id)
        category = self.category_collection.find_one({"_id": id})
        if not category:
            return False
        update_data = {}
        if name:
            update_data["name"] = name
        if url:
            update_data["url"] = url
        if articles:
            update_data["articles"] = articles
        if update_data:
            self.category_collection.update_one({"_id": id}, {"$set": update_data})
            return True
        return False

    def replace_category(self, id, name, url, articles):
        if not isinstance(id, ObjectId):
            id = ObjectId(id)
        category = self.category_collection.find_one({"_id": id})
        if not category:
            return False
        category_data = {
            "name": name,
            "url": url,
            "articles": articles
        }
        self.category_collection.replace_one({"_id": id}, category_data)
        return True

    def delete_category(self, id):
        if not isinstance(id, ObjectId):
            id = ObjectId(id)
        result = self.category_collection.delete_one({"_id": id})
        return result.deleted_count > 0
    
    def get_categories(self):
        return list(self.category_collection.find())
