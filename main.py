import tkinter as tk
from controller.user_controller import UserController
from controller.article_controller import ArticleController

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Blog")
        self.geometry("600x600")

        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)

        self.user_controller = UserController(self)
        self.article_controller = ArticleController(self)

        welcome_label = tk.Label(self.main_frame, text="Gestor de Base de datos \"Blog\"", font=("Helvetica", 16))
        welcome_label.pack(pady=20)

        users_button = tk.Button(self.main_frame, text="Usuarios", width=50, height=3, command=self.user_controller.view.display_user_crud)
        users_button.pack(pady=10)

        articles_button = tk.Button(self.main_frame, text="Artículos", width=50, height=3, command=self.article_controller.view.display_article_crud)
        articles_button.pack(pady=10)

        articles_button = tk.Button(self.main_frame, text="Artículos", width=50, height=3, command=self.article_controller.view.display_article_crud)
        articles_button.pack(pady=10)

        articles_button = tk.Button(self.main_frame, text="Artículos", width=50, height=3, command=self.article_controller.view.display_article_crud)
        articles_button.pack(pady=10)

        articles_button = tk.Button(self.main_frame, text="Artículos", width=50, height=3, command=self.article_controller.view.display_article_crud)
        articles_button.pack(pady=10)
    
    def clear_window(self):
        self.main_frame.pack_forget()
        # Only destroy child widgets without repacking main_frame
        #for widget in self.main_frame.winfo_children():
            #widget.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
