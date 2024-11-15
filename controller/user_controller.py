from controller.base_controller import BaseController
from model.user import UserModel
from view.user_view import UserView
from bson import ObjectId

class UserController(BaseController):
    def __init__(self, root):
        self.model = UserModel()
        self.view = UserView(root, self)
    
    def create_user(self, name, email, articles, comments):
        articles = [ObjectId(article) for article in articles if article]
        comments = [ObjectId(comment) for comment in comments if comment]
        
        if self.model.create_user(name, email, articles, comments):
            print("¡Usuario creado exitosamente con referencias de artículos!")

    def update_user(self, id, name, email, articles, comments):
        articles = [ObjectId(article) for article in articles if article]
        comments = [ObjectId(comment) for comment in comments if comment]

        if self.model.update_user(id, name, email, articles, comments):
            print("¡Usuario creado exitosamente con referencias de artículos!")

    def replace_user(self, id, name, email, articles, comments):
        articles = [ObjectId(article) for article in articles if article]
        comments = [ObjectId(comment) for comment in comments if comment]

        if self.model.replace_user(id, name, email, articles, comments):
            print("¡Usuario creado exitosamente con referencias de artículos!")

    def delete_user(self, id):
        if self.model.delete_user(id):
            print("Usuario Eliminado correctamete")

    def get_users(self):
        users_list = self.model.get_users()
        if users_list:
            return users_list
        else:
            print("Error: No se encontraron usuarios")
            return []



