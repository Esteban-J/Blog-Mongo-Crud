from pymongo import MongoClient
from bson import ObjectId

class UserModel:
    def __init__(self):
        self.db = MongoClient('mongodb://localhost:27017/')["blog"]
        self.users_collection = self.db["users"]

    def create_user(self, name, email, articles_ids, comments_ids):

        user_data = {
            "name": name,
            "email": email,
            "articles": articles_ids,
            "comments": comments_ids
        }

        self.users_collection.insert_one(user_data)
        return True

    def update_user(self, id, name=None, email=None, articles_ids=None, comments_ids=None):
        if not isinstance(id, ObjectId):
            id = ObjectId(id)
    
        user = self.users_collection.find_one({"_id": id})
        
        if not user:
            return False
        
        name = name if name is not "" else user.get("name")
        email = email if email is not "" else user.get("email")
        articles_ids = articles_ids if articles_ids is not "" else user.get("articles")
        comments_ids = comments_ids if comments_ids is not "" else user.get("comments")
    
        self.users_collection.update_one(
            {"_id": id},
            {"$set": {"name": name, "email": email, "articles": articles_ids, "comments": comments_ids}}
        )
        return True

    def replace_user(self, id, name=None, email=None, articles_ids=None, comments_ids=None):
        if not isinstance(id, ObjectId):
            id = ObjectId(id)
    
        user = self.users_collection.find_one({"_id": id})

        if not user:
            return False
    
        self.users_collection.update_one(
            {"_id": id},
            {"$set": {"name": name, "email": email, "articles": articles_ids, "comments": comments_ids}}
        )
        return True

    def delete_user(self, id):

        if not isinstance(id, ObjectId):
            id = ObjectId(id)
    
        result = self.users_collection.delete_one({"_id": id})
        
        return result.deleted_count > 0
    
    def get_users(self):
        return self.users_collection.find()
