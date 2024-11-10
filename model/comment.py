from pymongo import MongoClient
from bson import ObjectId

class CommentModel:
    def __init__(self):
        self.db = MongoClient('mongodb://localhost:27017/')["blog"]
        self.comment_collection = self.db["comment"]

    def create_comment(self, name, url, articles, user_id):
        comment_data = {
            "name": name,
            "url": url,
            "articles": articles,
            "user": user_id
        }

        self.comment_collection.insert_one(comment_data)
        return True

    def update_comment(self, id, name=None, url=None, articles=None, user_id=None):
        if not isinstance(id, ObjectId):
            id = ObjectId(id)
        
        comment = self.comment_collection.find_one({"_id": id})
        
        if not comment:
            return False
        
        name = name if name != "" else comment.get("name")
        url = url if url != "" else comment.get("url")
        articles = articles if articles != "" else comment.get("articles")
        user_id = user_id if user_id != "" else comment.get("user")

        self.comment_collection.update_one(
            {"_id": id},
            {"$set": {"name": name, "url": url, "articles": articles, "user": user_id}}
        )
        return True

    def replace_comment(self, id, name=None, url=None, articles=None, user_id=None):
        if not isinstance(id, ObjectId):
            id = ObjectId(id)
        
        comment = self.comment_collection.find_one({"_id": id})

        if not comment:
            return False

        self.comment_collection.update_one(
            {"_id": id},
            {"$set": {"name": name, "url": url, "articles": articles, "user": user_id}}
        )
        return True

    def delete_comment(self, id):
        if not isinstance(id, ObjectId):
            id = ObjectId(id)
        
        result = self.comment_collection.delete_one({"_id": id})
        
        return result.deleted_count > 0

    def get_comments(self):
        return list(self.comment_collection.find())
