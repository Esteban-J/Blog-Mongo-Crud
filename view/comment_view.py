import tkinter as tk
from view.base_view import BaseView
import tkinter.messagebox as messagebox
from bson.errors import InvalidId

class CommentView:
    def __init__(self, root, controller):
        self.controller = controller
        self.view = BaseView(root)
        self.root = root

    def display_comment_crud(self):
        self.root.main_frame.pack_forget()
        self.view.main_frame.pack(fill="both", expand=True)
        
        label = tk.Label(self.view.main_frame, text="Comentarios", font=("Helvetica", 16))
        label.pack(pady=20)

        buttons = [
            ("Crear", lambda: self.display_comment_form(1)),
            ("Actualizar", lambda: self.display_comment_form(2)),
            ("Remplazar", lambda: self.display_comment_form(3)),
            ("Eliminar", lambda: self.display_comment_form(4)),
            ("Regresar", self.back_to_main),
        ]

        for text, command in buttons:
            button = tk.Button(self.view.main_frame, text=text, width=50, height=3, command=command)
            button.pack(pady=10)

    def display_comment_form(self, num):
        form_classes = {
            1: CreateCommentForm,
            2: UpdateCommentForm,
            3: ReplaceCommentForm,
            4: DeleteCommentForm,
        }
        
        if num in form_classes:
            if num == 4:
                form_classes[num](self.view.main_frame, self.controller)
            else:
                form_classes[num](self.view.main_frame, self.controller, self.populate_common_widgets)


    def populate_common_widgets(self, parent, submit_command):
        name_label = tk.Label(parent, text="Nombre")
        name_label.pack(pady=5)
        name_input = tk.Entry(parent)
        name_input.pack(pady=5)

        url_label = tk.Label(parent, text="URL")
        url_label.pack(pady=5)
        url_input = tk.Entry(parent)
        url_input.pack(pady=5)

        articles_ids_label = tk.Label(parent, text="Artículos (IDs separados por comas)")
        articles_ids_label.pack(pady=5)
        articles_ids_input = tk.Entry(parent)
        articles_ids_input.pack(pady=5)

        user_id_label = tk.Label(parent, text="ID del Usuario")
        user_id_label.pack(pady=5)
        user_id_input = tk.Entry(parent)
        user_id_input.pack(pady=5)

        submit_button = tk.Button(parent, text="Enviar", width=50, height=3, command=submit_command)
        submit_button.pack(pady=10)

        return name_input, url_input, articles_ids_input, user_id_input
    
    def back_to_main(self):
        self.root.main_frame.pack(fill="both", expand=True)
        self.view.main_frame.destroy()
        self.view = BaseView(self.root)


class CreateCommentForm(tk.Toplevel):
    def __init__(self, parent, controller, populate_common_widgets):
        super().__init__(parent)
        self.controller = controller
        self.title("Crear Comentario")
        self.geometry("600x400")

        window_msg = tk.Label(self, text="Ingrese los datos del Comentario", font=("Helvetica", 16))
        window_msg.pack(pady=10)

        self.name_input, self.url_input, self.articles_ids_input, self.user_id_input = populate_common_widgets(self, self.submit_comment_data)

    def submit_comment_data(self):
        try:
            name = self.name_input.get().strip()
            url = self.url_input.get().strip()
            articles_ids = [article.strip() for article in self.articles_ids_input.get().split(",") if article.strip()]
            user_id = self.user_id_input.get().strip()
            self.controller.create_comment(name, url, articles_ids, user_id)
            messagebox.showinfo("Exito", "Comentario creado correctamente!")
        except InvalidId:
            messagebox.showerror("Error", "ID inválido: Debe de ser un ObjectId")
        except Exception as e:
            messagebox.showerror("Error", f"Un error ha ocurrido: {e}")


class UpdateCommentForm(tk.Toplevel):
    def __init__(self, parent, controller, populate_common_widgets):
        super().__init__(parent)
        self.controller = controller
        self.title("Actualizar datos de Comentario")
        self.geometry("600x500")

        window_msg1 = tk.Label(self, text="Ingrese el ID del comentario a actualizar", font=("Helvetica", 16))
        window_msg1.pack(pady=10)

        id_label = tk.Label(self, text="Id")
        id_label.pack(pady=5)
        self.id_input = tk.Entry(self)
        self.id_input.pack(pady=5)
        
        window_msg2 = tk.Label(self, text="Ingrese los nuevos datos del comentario", font=("Helvetica", 16))
        window_msg2.pack(pady=10)

        self.name_input, self.url_input, self.articles_ids_input, self.user_id_input = populate_common_widgets(self, self.submit_comment_data)

    def submit_comment_data(self):
        try:
            comment_id = self.id_input.get().strip()
            name = self.name_input.get().strip()
            url = self.url_input.get().strip()
            articles_ids = [article.strip() for article in self.articles_ids_input.get().split(",") if article.strip()]
            user_id = self.user_id_input.get().strip()
            self.controller.update_comment(comment_id, name, url, articles_ids, user_id)
            messagebox.showinfo("Exito", "Comentario actualizado correctamente!")
        except InvalidId:
            messagebox.showerror("Error", "ID inválido: Debe de ser un ObjectId")
        except Exception as e:
            messagebox.showerror("Error", f"Un error ha ocurrido: {e}")


class ReplaceCommentForm(tk.Toplevel):
    def __init__(self, parent, controller, populate_common_widgets):
        super().__init__(parent)
        self.controller = controller
        self.title("Remplazar datos de comentario")
        self.geometry("600x500")

        window_msg1 = tk.Label(self, text="Ingrese el ID del comentario a reemplazar", font=("Helvetica", 16))
        window_msg1.pack(pady=10)

        id_label = tk.Label(self, text="Id")
        id_label.pack(pady=5)
        self.id_input = tk.Entry(self)
        self.id_input.pack(pady=5)
        
        window_msg2 = tk.Label(self, text="Ingrese los nuevos datos del comentario", font=("Helvetica", 16))
        window_msg2.pack(pady=10)

        self.name_input, self.url_input, self.articles_ids_input, self.user_id_input = populate_common_widgets(self, self.submit_comment_data)

    def submit_comment_data(self):
        try:
            comment_id = self.id_input.get().strip()
            name = self.name_input.get().strip()
            url = self.url_input.get().strip()
            articles_ids = [article.strip() for article in self.articles_ids_input.get().split(",") if article.strip()]
            user_id = self.user_id_input.get().strip()
            self.controller.replace_comment(comment_id, name, url, articles_ids, user_id)
            messagebox.showinfo("Exito", "Comentario reemplazado correctamente!")
        except InvalidId:
            messagebox.showerror("Error", "ID inválido: Debe de ser un ObjectId")
        except Exception as e:
            messagebox.showerror("Error", f"Un error ha ocurrido: {e}")


class DeleteCommentForm(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.title("Eliminar comentario")
        self.geometry("600x200")

        window_msg = tk.Label(self, text="Ingrese el ID del comentario a eliminar", font=("Helvetica", 16))
        window_msg.pack(pady=10)

        id_label = tk.Label(self, text="Id")
        id_label.pack(pady=5)
        self.id_input = tk.Entry(self)
        self.id_input.pack(pady=5)

        submit_button = tk.Button(self, text="Eliminar", width=50, height=3, command=self.submit_comment_data)
        submit_button.pack(pady=10)

    def submit_comment_data(self):
        try:
            comment_id = self.id_input.get().strip()
            self.controller.delete_comment(comment_id)
            messagebox.showinfo("Exito", "Comentario eliminado correctamente!")
        except InvalidId:
            messagebox.showerror("Error", "ID inválido: Debe de ser un ObjectId")
        except Exception as e:
            messagebox.showerror("Error", f"Un error ha ocurrido: {e}")

