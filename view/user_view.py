import tkinter as tk
from view.base_view import BaseView

class UserView:
    def __init__(self, root, controller):
        self.controller = controller
        self.view = BaseView(root)
        self.root = root

    def display_user_crud(self):
        self.root.clear_window()

        label = tk.Label(self.view.main_frame, text="Usuarios", font=("Helvetica", 16))
        label.pack(pady=20)

        create_button = tk.Button(self.view.main_frame, text="Crear", width=50, height=3, command=lambda: self.display_user_form(1))
        create_button.pack(pady=10)

        update_button = tk.Button(self.view.main_frame, text="Actualizar", width=50, height=3, command=lambda: self.display_user_form(2))
        update_button.pack(pady=10)

        replace_button = tk.Button(self.view.main_frame, text="Remplazar", width=50, height=3, command=lambda: self.display_user_form(3))
        replace_button.pack(pady=10)

        delete_button = tk.Button(self.view.main_frame, text="Eliminar", width=50, height=3, command=lambda: self.display_user_form(4))
        delete_button.pack(pady=10)

        get_button = tk.Button(self.view.main_frame, text="Ver lista", width=50, height=3, command=lambda: self.display_user_form(5))
        get_button.pack(pady=10)

    def display_user_form(self, num):
        match num:
            case 1:
                CreateFormInput(self.view.main_frame, self.controller)
            case 2:
                UpdateFormInput(self.view.main_frame, self.controller)
            case 3:
                ReplaceFormInput(self.view.main_frame, self.controller)
            case 4:
                DeleteFormInput(self.view.main_frame, self.controller)

class CreateFormInput(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.title("Datos nuevo usuario")
        self.geometry("600x400")

        window_msg = tk.Label(self, text="Ingrese los datos del usuario", font=("Helvetica", 16))
        window_msg.pack(pady=10)

        name_label = tk.Label(self, text="Nombre")
        name_label.pack(pady=5)
        self.name_input = tk.Entry(self)
        self.name_input.pack(pady=5)

        email_label = tk.Label(self, text="Email")
        email_label.pack(pady=5)
        self.email_input = tk.Entry(self)
        self.email_input.pack(pady=5)

        articles_ids_label = tk.Label(self, text="Artículos (IDs separados por comas)")
        articles_ids_label.pack(pady=5)
        self.articles_ids_input = tk.Entry(self)
        self.articles_ids_input.pack(pady=5)

        comments_ids_label = tk.Label(self, text="Comentarios (IDs separados por comas)")
        comments_ids_label.pack(pady=5)
        self.comments_ids_input = tk.Entry(self)
        self.comments_ids_input.pack(pady=5)

        submit_button = tk.Button(self, text="Crear", width=50, height=3, command=self.submit_user_data)
        submit_button.pack(pady=10)

    def submit_user_data(self):
        name = self.name_input.get().strip()
        email = self.email_input.get().strip()
        articles_ids = [article.strip() for article in self.articles_ids_input.get().split(",") if article.strip()]
        comments_ids = [comment.strip() for comment in self.comments_ids_input.get().split(",") if comment.strip()]
        self.controller.create_user(name, email, articles_ids, comments_ids)

class UpdateFormInput(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.title("Actualizar datos de usuario")
        self.geometry("600x400")

        window_msg1 = tk.Label(self, text="Ingrese el ID del usuario a actualizar", font=("Helvetica", 16))
        window_msg1.pack(pady=10)

        id_label = tk.Label(self, text="Id")
        id_label.pack(pady=5)
        self.id_input = tk.Entry(self)
        self.id_input.pack(pady=5)
        
        window_msg2 = tk.Label(self, text="Ingrese los nuevos datos del usuario", font=("Helvetica", 16))
        window_msg2.pack(pady=10)

        name_label = tk.Label(self, text="Nombre")
        name_label.pack(pady=5)
        self.name_input = tk.Entry(self)
        self.name_input.pack(pady=5)

        email_label = tk.Label(self, text="Email")
        email_label.pack(pady=5)
        self.email_input = tk.Entry(self)
        self.email_input.pack(pady=5)

        articles_ids_label = tk.Label(self, text="Artículos (IDs separados por comas)")
        articles_ids_label.pack(pady=5)
        self.articles_ids_input = tk.Entry(self)
        self.articles_ids_input.pack(pady=5)

        comments_ids_label = tk.Label(self, text="Comentarios (IDs separados por comas)")
        comments_ids_label.pack(pady=5)
        self.comments_ids_input = tk.Entry(self)
        self.comments_ids_input.pack(pady=5)

        submit_button = tk.Button(self, text="Actualizar", width=50, height=3, command=self.submit_user_data)
        submit_button.pack(pady=10)

    def submit_user_data(self):
        id = self.id_input.get().strip()
        name = self.name_input.get().strip()
        email = self.email_input.get().strip()
        articles_ids = [article.strip() for article in self.articles_ids_input.get().split(",") if article.strip()]
        comments = [comment.strip() for comment in self.comments_ids_input.get().split(",") if comment.strip()]
        self.controller.update_user(id, name, email, articles_ids, comments)

class ReplaceFormInput(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.title("Remplazar usuario")
        self.geometry("600x400")

        window_msg1 = tk.Label(self, text="Ingrese el ID del usuario a remplazar", font=("Helvetica", 16))
        window_msg1.pack(pady=10)

        id_label = tk.Label(self, text="Id")
        id_label.pack(pady=5)
        self.id_input = tk.Entry(self)
        self.id_input.pack(pady=5)

        window_msg2 = tk.Label(self, text="Ingrese los datos del usuario nuevo", font=("Helvetica", 16))
        window_msg2.pack(pady=10)

        name_label = tk.Label(self, text="Nombre")
        name_label.pack(pady=5)
        self.name_input = tk.Entry(self)
        self.name_input.pack(pady=5)

        email_label = tk.Label(self, text="Email")
        email_label.pack(pady=5)
        self.email_input = tk.Entry(self)
        self.email_input.pack(pady=5)

        articles_ids_label = tk.Label(self, text="Artículos (IDs separados por comas)")
        articles_ids_label.pack(pady=5)
        self.articles_ids_input = tk.Entry(self)
        self.articles_ids_input.pack(pady=5)

        comments_ids_label = tk.Label(self, text="Comentarios (IDs separados por comas)")
        comments_ids_label.pack(pady=5)
        self.comments_ids_input = tk.Entry(self)
        self.comments_ids_input.pack(pady=5)

        submit_button = tk.Button(self, text="Remplazar", width=50, height=3, command=self.submit_user_data)
        submit_button.pack(pady=10)

    def submit_user_data(self):
        id = self.id_input.get().strip()
        name = self.name_input.get().strip()
        email = self.email_input.get().strip()
        articles_ids = [article.strip() for article in self.articles_ids_input.get().split(",") if article.strip()]
        comments = [comment.strip() for comment in self.comments_ids_input.get().split(",") if comment.strip()]
        self.controller.replace_user(id, name, email, articles_ids, comments)

class DeleteFormInput(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.title("Eliminar usuario")
        self.geometry("600x200")

        window_msg = tk.Label(self, text="Ingrese el ID del usuario a eliminar", font=("Helvetica", 16))
        window_msg.pack(pady=10)

        id_label = tk.Label(self, text="Id")
        id_label.pack(pady=5)
        self.id_input = tk.Entry(self)
        self.id_input.pack(pady=5)

        submit_button = tk.Button(self, text="Eliminar", width=50, height=3, command=self.submit_user_data)
        submit_button.pack(pady=10)

    def submit_user_data(self):
        id = self.id_input.get().strip()
        self.controller.delete_user(id)

