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
            ("Consultar", lambda: self.display_comment_form(5)),
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
            5: ShowComments
        }
        
        if num in form_classes:
            if num == 4 or num == 5:
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

class ShowComments(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.title("Mostrar comentarios")
        self.geometry("600x400")

        search_frame = tk.Frame(self)
        search_frame.pack(pady=5)

        tk.Label(search_frame, text="ID del comentario:").pack(side="left", padx=5)
        self.comment_id_entry = tk.Entry(search_frame)
        self.comment_id_entry.pack(side="left", padx=5)
        search_button = tk.Button(search_frame, text="Buscar", command=self.search_comment_by_id)
        search_button.pack(side="left", padx=5)

        refresh_button = tk.Button(self, text="Refrescar", command=self.refresh_data)
        refresh_button.pack(pady=5)

        self.canvas = tk.Canvas(self)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollable_frame = tk.Frame(self.canvas)
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="top", fill="both", expand=True)

        self.pagination_frame = tk.Frame(self)
        self.pagination_frame.pack(pady=5)

        self.comments_per_page = 5 
        self.current_page = 0

        self.comments = self.controller.get_comments()
        self.total_comments = len(self.comments)
        self.display_comments_page()

    def refresh_data(self):
        self.current_page = 0
        self.comments = self.controller.get_comments()
        self.total_comments = len(self.comments)
        self.display_comments_page()

    def search_comment_by_id(self):
        comment_id = self.comment_id_entry.get().strip()

        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        comment = next((comment for comment in self.comments if str(comment['_id']) == comment_id), None)

        if comment:
            comment_text = f"ID del comment: {comment['_id']}\nNombre: {comment['name']}\nurl: {comment['url']}\nArtículos: {comment['articles']}"
            comment_display = tk.Text(self.scrollable_frame, height=4, wrap="word")
            comment_display.insert("1.0", comment_text)
            comment_display.configure(state="disabled")
            comment_display.pack(pady=5)
        else:
            self.display_comments_page()
            messagebox.showerror("Error", "Comentario no encontrado")

        self.scrollable_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def display_comments_page(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        start_index = self.current_page * self.comments_per_page
        end_index = min(start_index + self.comments_per_page, self.total_comments)

        for i in range(start_index, end_index):
            comment = self.comments[i]
            comment_text = f"ID de Usuario: {comment['_id']}\nNombre: {comment['name']}\nurl: {comment['url']}\nArtículos: {comment['articles']}"
            comment_display = tk.Text(self.scrollable_frame, height=6, wrap="word")
            comment_display.insert("1.0", comment_text)
            comment_display.configure(state="disabled")
            comment_display.pack(pady=5, fill="both", expand=True)

        self.scrollable_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        self.create_pagination_buttons()

    def create_pagination_buttons(self):
        for widget in self.pagination_frame.winfo_children():
            widget.destroy()

        if self.current_page > 0:
            prev_button = tk.Button(self.pagination_frame, text="Previous", command=self.prev_page)
            prev_button.pack(side="left", padx=10)

        if self.current_page < (self.total_comments // self.comments_per_page):
            next_button = tk.Button(self.pagination_frame, text="Next", command=self.next_page)
            next_button.pack(side="left", padx=10)

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.display_comments_page()

    def next_page(self):
        if (self.current_page + 1) * self.comments_per_page < self.total_comments:
            self.current_page += 1
            self.display_comments_page()
