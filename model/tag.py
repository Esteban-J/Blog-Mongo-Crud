from pymongo import MongoClient
from bson import ObjectId

class TagModel:
    def __init__(self):
        self.db = MongoClient('mongodb://localhost:27017/')["blog"]
        self.tag_collection = self.db["tag"]

    def create_tag(self, name, articles):
        tag_data = {
            "name": name,
            "articles": articles
        }
        
        self.tag_collection.insert_one(tag_data)
        return True

    def update_tag(self, id, name=None, articles=None):
        if not isinstance(id, ObjectId):
            id = ObjectId(id)

        tag = self.tag_collection.find_one({"_id": id})
        if not tag:
            return False

        update_data = {}
        if name is not None:
            update_data["name"] = name
        if articles is not None:
            update_data["articles"] = articles

        if update_data:
            self.tag_collection.update_one({"_id": id}, {"$set": update_data})
            return True
        return False

    def replace_tag(self, id, name, articles):
        if not isinstance(id, ObjectId):
            id = ObjectId(id)

        tag = self.tag_collection.find_one({"_id": id})
        if not tag:
            return False

        tag_data = {
            "name": name,
            "articles": articles
        }

        self.tag_collection.replace_one({"_id": id}, tag_data)
        return True

    def delete_tag(self, id):
        if not isinstance(id, ObjectId):
            id = ObjectId(id)

        result = self.tag_collection.delete_one({"_id": id})
        return result.deleted_count > 0
