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
            print("¡Comentario creado exitosamente con referencias de artículo y usuario!")

    def update_comment(self, id, name, url, articles, user_id):
        user_id = ObjectId(user_id) if user_id else None
        articles = [ObjectId(article) for article in articles if article]

        if self.model.update_comment(id, name, url, articles, user_id):
            print("¡Comentario creado exitosamente con referencias de artículo y usuario!")

    def replace_comment(self, id, name, url, articles, user_id):
        user_id = ObjectId(user_id) if user_id else None
        articles = [ObjectId(article) for article in articles if article]

        if self.model.replace_comment(id, name, url, articles, user_id):
            print("¡Comentario creado exitosamente con referencias de artículo y usuario!")


    def delete_comment(self, id):
        if self.model.delete_comment(id):
            print("Comentario eliminado exitosamente")
    
    def get_comments(self):
        comments_list = self.model.get_comments()
        if comments_list:
            return comments_list
        else:
            print("Error: No se encontraron comentarios")
            return []
