from controller.base_controller import BaseController
from model.comment import CommentModel
from view.comment_view import CommentView
from bson import ObjectId
import tkinter.messagebox as messagebox


class CommentController(BaseController):
    def __init__(self, root):
        self.model = CommentModel()
        self.view = CommentView(root, self)

    def create_comment(self, name, url, articles, user_id):
        user_id = ObjectId(user_id) if user_id else None
        articles = [ObjectId(article) for article in articles if article]

        if self.model.create_comment(name, url, articles, user_id):
            print("Comment created successfully with article and user references!")
        else:
            print("Error: Missing required fields for comment creation")

    def update_comment(self, id, name, url, articles, user_id):
        user_id = ObjectId(user_id) if user_id else None
        articles = [ObjectId(article) for article in articles if article]

        if self.model.update_comment(id, name, url, articles, user_id):
            print("Comment updated successfully with article and user references!")
        else:
            print("Error: Failed to update comment or comment not found")

    def replace_comment(self, id, name, url, articles, user_id):
        user_id = ObjectId(user_id) if user_id else None
        articles = [ObjectId(article) for article in articles if article]

        if self.model.replace_comment(id, name, url, articles, user_id):
            print("Comment replaced successfully with article and user references!")
        else:
            print("Error: Failed to replace comment or comment not found")

    def delete_comment(self, id):
        if self.model.delete_comment(id):
            print("Comment deleted successfully")
        else:
            print("Error: Failed to delete comment or comment not found")
