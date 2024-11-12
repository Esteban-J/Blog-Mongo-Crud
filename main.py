import tkinter as tk
import subprocess
import os
import time
import atexit

from controller.user_controller import UserController
from controller.article_controller import ArticleController
from controller.comment_controller import CommentController
from controller.tag_controller import TagController
from controller.category_controller import CategoryController


def start_mongo():
    """Inicia el servidor de MongoDB."""
    mongo_path = "C:/Program Files/MongoDB/Server/8.0/bin/mongod.exe"
    data_path = "C:/data/db"
    os.makedirs(data_path, exist_ok=True)
    
    # Inicia el proceso de MongoDB
    process = subprocess.Popen([mongo_path, "--dbpath", data_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Espera un momento para que MongoDB termine de iniciar
    time.sleep(2)
    print("MongoDB iniciado.")
    return process

def stop_mongo(process):
    """Detiene el servidor de MongoDB."""
    process.terminate()
    process.wait()
    print("MongoDB detenido.")


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Blog")
        self.geometry("600x600")

        # Crea el marco principal para la interfaz de usuario
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)

        # Importa los controladores para los diferentes modelos
        self.user_controller = UserController(self)
        self.article_controller = ArticleController(self)
        self.comment_controller = CommentController(self)
        self.tag_controller = TagController(self)
        self.category_controller = CategoryController(self)

        # Configura los elementos de la interfaz de usuario
        welcome_label = tk.Label(self.main_frame, text="Gestor de Base de datos \"Blog\"", font=("Helvetica", 16))
        welcome_label.pack(pady=20)

        users_button = tk.Button(self.main_frame, text="Usuarios", width=50, height=3, command=self.user_controller.view.display_user_crud)
        users_button.pack(pady=10)

        articles_button = tk.Button(self.main_frame, text="Artículos", width=50, height=3, command=self.article_controller.view.display_article_crud)
        articles_button.pack(pady=10)

        comments_button = tk.Button(self.main_frame, text="Comentarios", width=50, height=3, command=self.comment_controller.view.display_comment_crud)
        comments_button.pack(pady=10)

        tags_button = tk.Button(self.main_frame, text="Tags", width=50, height=3, command=self.tag_controller.view.display_tag_crud)
        tags_button.pack(pady=10)

        categories_button = tk.Button(self.main_frame, text="Categoría", width=50, height=3, command=self.category_controller.view.display_category_crud)
        categories_button.pack(pady=10)


if __name__ == "__main__":
    # Inicia MongoDB
    mongo_process = start_mongo()

    # Registra stop_mongo para que se ejecute al cerrar la aplicación
    atexit.register(stop_mongo, mongo_process)

    # Inicia la aplicación Tkinter
    app = App()
    app.mainloop()
