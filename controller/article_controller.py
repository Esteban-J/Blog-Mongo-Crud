from controller.base_controller import BaseController
from model.article import ArticleModel
from view.article_view import ArticleView
from bson import ObjectId
import tkinter.messagebox as messagebox


class ArticleController(BaseController):
    def __init__(self, root):
        self.model = ArticleModel()
        self.view = ArticleView(root, self)
    
    def create_article(self, title, date, text,  user_id, comments):
        user_id = ObjectId(user_id) if user_id else None
        comments = [ObjectId(comment) if comment else None for comment in comments]

        if self.model.create_article(title, date, text, user_id, comments):
            print("article created successfully with article references!")
        else:
            print("Error: Missing articletitle, date, or articles")

    def update_article(self, id, title, date, text, user_id, comments):
        user_id = ObjectId(user_id) if user_id else None
        comments = [ObjectId(comment) for comment in comments if comment]
        

        if self.model.update_article(id, title, date, text, user_id, comments):
            print("article updated successfully with article references!")
        else:
            print("Error: Missing articletitle, date, or articles")

    def replace_article(self, id, title, date, text, user_id, comments):
        user_id = ObjectId(user_id) if user_id else None
        comments = [ObjectId(comment) for comment in comments if comment]

        if self.model.replace_article(id, title, date, text, user_id, comments):
            print("article updated successfully with article references!")
        else:
            print("Error: Missing articletitle, date, or articles")

    def delete_article(self, id):
        if self.model.delete_article(id):
            print("Usuario Eliminado correctamete")
        else:
            print("Error")

