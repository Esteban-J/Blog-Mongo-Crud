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
            print("User created successfully with article references!")
        else:
            print("Error: Missing username, email, or articles")

    def update_user(self, id, name, email, articles, comments):
        articles = [ObjectId(article) for article in articles if article]
        comments = [ObjectId(comment) for comment in comments if comment]

        if self.model.update_user(id, name, email, articles, comments):
            print("User updated successfully with article references!")
        else:
            print("Error: Missing username, email, or articles")

    def replace_user(self, id, name, email, articles, comments):
        articles = [ObjectId(article) for article in articles if article]
        comments = [ObjectId(comment) for comment in comments if comment]

        if self.model.replace_user(id, name, email, articles, comments):
            print("User updated successfully with article references!")
        else:
            print("Error: Missing username, email, or articles")

    def delete_user(self, id):
        if self.model.delete_user(id):
            print("Usuario Eliminado correctamete")
        else:
            print("Error")

