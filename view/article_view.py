import tkinter as tk

from view.base_view import BaseView

class ArticleView:
    def __init__(self, root, controller):
        self.controller = controller
        self.view = BaseView(root)

    def display_article_crud(self):
        self.view.clear_window()

        label = tk.Label(self.view.main_frame, text="Artículos", font=("Helvetica", 16))
        label.pack(pady=20)

        create_button = tk.Button(self.view.main_frame, text="Crear", width=50, height=3, command=self.controller.create_article)
        create_button.pack(pady=10)

        # Add other CRUD buttons here (update, delete)
