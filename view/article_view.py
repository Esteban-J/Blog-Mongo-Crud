import tkinter as tk
from view.base_view import BaseView
from tkcalendar import DateEntry 

class ArticleView:
    def __init__(self, root, controller):
        self.controller = controller
        self.view = BaseView(root)
        self.root = root

    def display_article_crud(self):
        self.root.clear_window()

        label = tk.Label(self.view.main_frame, text="Artículos", font=("Helvetica", 16))
        label.pack(pady=20)

        create_button = tk.Button(self.view.main_frame, text="Crear", width=50, height=3, command=lambda: self.display_article_form(1))
        create_button.pack(pady=10)

        update_button = tk.Button(self.view.main_frame, text="Actualizar", width=50, height=3, command=lambda: self.display_article_form(2))
        update_button.pack(pady=10)

        replace_button = tk.Button(self.view.main_frame, text="Remplazar", width=50, height=3, command=lambda: self.display_article_form(3))
        replace_button.pack(pady=10)

        delete_button = tk.Button(self.view.main_frame, text="Eliminar", width=50, height=3, command=lambda: self.display_article_form(4))
        delete_button.pack(pady=10)

        get_button = tk.Button(self.view.main_frame, text="Ver lista", width=50, height=3, command=lambda: self.display_article_form(5))
        get_button.pack(pady=10)

    def display_article_form(self, num):
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
        self.title("Datos nuevo artículo")
        self.geometry("600x400")

        window_msg = tk.Label(self, text="Ingrese los datos del artículo", font=("Helvetica", 16))
        window_msg.pack(pady=10)

        title_label = tk.Label(self, text="Nombre")
        title_label.pack(pady=5)
        self.title_input = tk.Entry(self)
        self.title_input.pack(pady=5)

        date_label = tk.Label(self, text="Fecha")
        date_label.pack(pady=5)
        self.date_input = DateEntry(self, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern="yyyy-mm-dd")
        self.date_input.pack(pady=5)

        user_id_label = tk.Label(self, text="Id del Usuario")
        user_id_label.pack(pady=5)
        self.user_id_input = tk.Entry(self)
        self.user_id_input.pack(pady=5)

        comments_ids_label = tk.Label(self, text="Comentarios (IDs separados por comas)")
        comments_ids_label.pack(pady=5)
        self.comments_ids_input = tk.Entry(self)
        self.comments_ids_input.pack(pady=5)

        submit_button = tk.Button(self, text="Crear", width=50, height=3, command=self.submit_article_data)
        submit_button.pack(pady=10)

    def submit_article_data(self):
        title = self.title_input.get()
        date = self.date_input.get()
        user_id = self.user_id_input.get()
        comments_ids = [comment.strip() for comment in self.comments_ids_input.get().split(",") if comment.strip()]
        self.controller.create_article(title, date, user_id, comments_ids)

class UpdateFormInput(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.title("Actualizar datos de artículo")
        self.geometry("600x400")

        window_msg1 = tk.Label(self, text="Ingrese el ID del artículo a actualizar", font=("Helvetica", 16))
        window_msg1.pack(pady=10)

        id_label = tk.Label(self, text="Id")
        id_label.pack(pady=5)
        self.id_input = tk.Entry(self)
        self.id_input.pack(pady=5)
        
        window_msg2 = tk.Label(self, text="Ingrese los nuevos datos del artículo", font=("Helvetica", 16))
        window_msg2.pack(pady=10)

        title_label = tk.Label(self, text="Nombre")
        title_label.pack(pady=5)
        self.title_input = tk.Entry(self)
        self.title_input.pack(pady=5)

        date_label = tk.Label(self, text="Fecha")
        date_label.pack(pady=5)
        self.date_input = DateEntry(self, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern="yyyy-mm-dd")
        self.date_input.pack(pady=5)

        user_id_label = tk.Label(self, text="Id del Usuario")
        user_id_label.pack(pady=5)
        self.user_id_input = tk.Entry(self)
        self.user_id_input.pack(pady=5)

        comments_ids_label = tk.Label(self, text="Comentarios (IDs separados por comas)")
        comments_ids_label.pack(pady=5)
        self.comments_ids_input = tk.Entry(self)
        self.comments_ids_input.pack(pady=5)

        submit_button = tk.Button(self, text="Actualizar", width=50, height=3, command=self.submit_article_data)
        submit_button.pack(pady=10)

    def submit_article_data(self):
        id = self.id_input.get()
        title = self.title_input.get()
        date = self.date_input.get()
        user_id = self.user_id_input.get()
        comments_ids = [comment.strip() for comment in self.comments_ids_input.get().split(",") if comment.strip()]
        self.controller.update_article(id, title, date, user_id, comments_ids)

class ReplaceFormInput(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.title("Remplazar artículo")
        self.geometry("600x400")

        window_msg1 = tk.Label(self, text="Ingrese el ID del artículo a remplazar", font=("Helvetica", 16))
        window_msg1.pack(pady=10)

        id_label = tk.Label(self, text="Id")
        id_label.pack(pady=5)
        self.id_input = tk.Entry(self)
        self.id_input.pack(pady=5)

        window_msg2 = tk.Label(self, text="Ingrese los datos del artículo nuevo", font=("Helvetica", 16))
        window_msg2.pack(pady=10)

        title_label = tk.Label(self, text="Nombre")
        title_label.pack(pady=5)
        self.title_input = tk.Entry(self)
        self.title_input.pack(pady=5)

        date_label = tk.Label(self, text="Fecha")
        date_label.pack(pady=5)
        self.date_input = DateEntry(self, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern="yyyy-mm-dd")
        self.date_input.pack(pady=5)

        user_id_label = tk.Label(self, text="Id del Usuario")
        user_id_label.pack(pady=5)
        self.user_id_input = tk.Entry(self)
        self.user_id_input.pack(pady=5)

        comments_ids_label = tk.Label(self, text="Comentarios (IDs separados por comas)")
        comments_ids_label.pack(pady=5)
        self.comments_ids_input = tk.Entry(self)
        self.comments_ids_input.pack(pady=5)

        submit_button = tk.Button(self, text="Remplazar", width=50, height=3, command=self.submit_article_data)
        submit_button.pack(pady=10)

    def submit_article_data(self):
        id_input = self.id_input.get()
        title = self.title_input.get()
        date = self.date_input.get()
        user_id = self.user_id_input.get()
        comments = [comment.strip() for comment in self.comments_ids_input.get().split(",") if comment.strip()]
        self.controller.replace_article(id_input, title, date, user_id, comments)

class DeleteFormInput(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.title("Eliminar artículo")
        self.geometry("600x200")

        window_msg = tk.Label(self, text="Ingrese el ID del artículo a eliminar", font=("Helvetica", 16))
        window_msg.pack(pady=10)

        id_label = tk.Label(self, text="Id")
        id_label.pack(pady=5)
        self.id_input = tk.Entry(self)
        self.id_input.pack(pady=5)

        submit_button = tk.Button(self, text="Eliminar", width=50, height=3, command=self.submit_article_data)
        submit_button.pack(pady=10)

    def submit_article_data(self):
        id = self.id_input.get()
        self.controller.delete_article(id)

