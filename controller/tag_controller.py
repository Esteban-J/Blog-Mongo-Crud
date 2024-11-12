from controller.base_controller import BaseController
from model.tag import TagModel
from view.tag_view import TagView
from bson import ObjectId
import tkinter.messagebox as messagebox


class TagController(BaseController):
    def __init__(self, root):
        self.model = TagModel()
        self.view = TagView(root, self)

    def create_tag(self, name, url, articles):
        articles = [ObjectId(article) for article in articles if article]

        if self.model.create_tag(name, url, articles):
            print("¡Etiqueta creada exitosamente con referencias de artículos!")

    def update_tag(self, id, name, url, articles):
        articles = [ObjectId(article) for article in articles if article]

        if self.model.update_tag(id, name, url, articles):
            print("¡Etiqueta creada exitosamente con referencias de artículos!")

    def replace_tag(self, id, name, url, articles):
        articles = [ObjectId(article) for article in articles if article]

        if self.model.replace_tag(id, name, url, articles):
            print("¡Etiqueta creada exitosamente con referencias de artículos!")

    def delete_tag(self, id):
        if self.model.delete_tag(id):
            print("Etiqueta eliminada exitosamente")

    def get_tags(self):
        tags_list = self.model.get_tags()
        if tags_list:
            return tags_list
        else:
            print("Error: No se encontraron etiquetas")
            return []

