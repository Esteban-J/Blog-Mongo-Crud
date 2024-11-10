from controller.base_controller import BaseController
from model.tag import TagModel
from view.tag_view import TagView
from bson import ObjectId
import tkinter.messagebox as messagebox


class TagController(BaseController):
    def __init__(self, root):
        self.model = TagModel()
        self.view = TagView(root, self)

    def create_tag(self, name, articles):
        articles = [ObjectId(article) for article in articles if article]

        if self.model.create_tag(name, articles):
            print("Tag created successfully with article references!")
        else:
            print("Error: Missing required fields for tag creation")

    def update_tag(self, id, name, articles):
        articles = [ObjectId(article) for article in articles if article]

        if self.model.update_tag(id, name, articles):
            print("Tag updated successfully with article references!")
        else:
            print("Error: Failed to update tag or tag not found")

    def replace_tag(self, id, name, articles):
        articles = [ObjectId(article) for article in articles if article]

        if self.model.replace_tag(id, name, articles):
            print("Tag replaced successfully with article references!")
        else:
            print("Error: Failed to replace tag or tag not found")

    def delete_tag(self, id):
        if self.model.delete_tag(id):
            print("Tag deleted successfully")
        else:
            print("Error: Failed to delete tag or tag not found")
