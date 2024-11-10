import tkinter as tk
from controller.user_controller import UserController
from controller.article_controller import ArticleController
from controller.comment_controller import CommentController
from controller.tag_controller import TagController


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Blog")
        self.geometry("600x600")

        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)

        self.user_controller = UserController(self)
        self.article_controller = ArticleController(self)
        self.comment_controller = CommentController(self)
        self.tag_controller = TagController(self)

        welcome_label = tk.Label(self.main_frame, text="Gestor de Base de datos \"Blog\"", font=("Helvetica", 16))
        welcome_label.pack(pady=20)

        users_button = tk.Button(self.main_frame, text="Usuarios", width=50, height=3, command=self.user_controller.view.display_user_crud)
        users_button.pack(pady=10)

        articles_button = tk.Button(self.main_frame, text="Artículos", width=50, height=3, command=self.article_controller.view.display_article_crud)
        articles_button.pack(pady=10)

        articles_button = tk.Button(self.main_frame, text="Comentarios", width=50, height=3, command=self.comment_controller.view.display_comment_crud)
        articles_button.pack(pady=10)

        articles_button = tk.Button(self.main_frame, text="Tags", width=50, height=3, command=self.tag_controller.view.display_tag_crud)
        articles_button.pack(pady=10)

        articles_button = tk.Button(self.main_frame, text="Artículos", width=50, height=3, command=self.article_controller.view.display_article_crud)
        articles_button.pack(pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()
