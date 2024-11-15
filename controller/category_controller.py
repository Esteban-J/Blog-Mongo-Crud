from controller.base_controller import BaseController
from model.category import CategoryModel
from view.category_view import CategoryView
from bson import ObjectId
import tkinter.messagebox as messagebox

class CategoryController(BaseController):
    def __init__(self, root):
        self.model = CategoryModel()
        self.view = CategoryView(root, self)

    def create_category(self, name, url, articles):
        articles = [ObjectId(article) for article in articles if article]
        if self.model.create_category(name, url, articles):
            print("Categoría creada correctamente!")

    def update_category(self, id, name, url, articles):
        articles = [ObjectId(article) for article in articles if article]
        if self.model.update_category(id, name, url, articles):
            print("Categoría actualizada correctamente!")

    def replace_category(self, id, name, url, articles):
        articles = [ObjectId(article) for article in articles if article]
        if self.model.replace_category(id, name, url, articles):
            print("Categoría reemplazada correctamente!")

    def delete_category(self, id):
        if self.model.delete_category(id):
            print("Categoría eliminada correctamente!")
        else:
            print("Error al eliminar la categoría")
    
    def get_categories(self):
        categories_list = self.model.get_categories()
        if categories_list:
            return categories_list
        else:
            print("Error: No se encontraron categorías")
            return []
