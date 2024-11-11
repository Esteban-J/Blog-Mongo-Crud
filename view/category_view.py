import tkinter as tk
from view.base_view import BaseView
from tkinter import messagebox
from bson.errors import InvalidId

class CategoryView:
    def __init__(self, root, controller):
        self.controller = controller
        self.view = BaseView(root)
        self.root = root

    def display_category_crud(self):
        self.root.main_frame.pack_forget()
        self.view.main_frame.pack(fill="both", expand=True)
    
        label = tk.Label(self.view.main_frame, text="Categorías", font=("Helvetica", 16))
        label.pack(pady=20)
        buttons = [
            ("Crear", lambda: self.display_category_form(1)),
            ("Actualizar", lambda: self.display_category_form(2)),
            ("Remplazar", lambda: self.display_category_form(3)),
            ("Eliminar", lambda: self.display_category_form(4)),
            ("Ver lista", lambda: self.display_category_form(5)),
        ]
        for text, command in buttons:
            button = tk.Button(self.view.main_frame, text=text, width=50, height=3, command=command)
            button.pack(pady=10)

    def display_category_form(self, num):
        form_classes = {
            1: CreateCategoryForm,
            2: UpdateCategoryForm,
            3: ReplaceCategoryForm,
            4: DeleteCategoryForm,
        }
        
        if num in form_classes:
            if num == 4:
                form_classes[num](self.view.main_frame, self.controller)
            else:
                form_classes[num](self.view.main_frame, self.controller, self.populate_common_widgets)


    def populate_common_widgets(self, parent, submit_command):
        name_label = tk.Label(parent, text="Nombre de la Categoría")
        name_label.pack(pady=5)
        name_input = tk.Entry(parent)
        name_input.pack(pady=5)

        url_label = tk.Label(parent, text="URL")
        url_label.pack(pady=5)
        url_input = tk.Entry(parent)
        url_input.pack(pady=5)

        articles_label = tk.Label(parent, text="Artículos (IDs separados por comas)")
        articles_label.pack(pady=5)
        articles_input = tk.Entry(parent)
        articles_input.pack(pady=5)

        submit_button = tk.Button(parent, text="Enviar", width=50, height=3, command=submit_command)
        submit_button.pack(pady=10)
        return name_input, url_input, articles_input


class CreateCategoryForm(tk.Toplevel):
    def __init__(self, parent, controller, populate_common_widgets):
        super().__init__(parent)
        self.controller = controller
        self.title("Crear Categoría")
        self.geometry("600x300")

        window_msg = tk.Label(self, text="Ingrese los datos de la categoría", font=("Helvetica", 16))
        window_msg.pack(pady=10)

        self.name_input, self.url_input, self.articles_input = populate_common_widgets(self, self.submit_category_data)

    def submit_category_data(self):
        try:
            name = self.name_input.get().strip()
            url = self.url_input.get().strip()
            articles = [article.strip() for article in self.articles_input.get().split(",") if article.strip()]
            self.controller.create_category(name, url, articles)
            messagebox.showinfo("Exito", "Categoría creado correctamente!")
        except InvalidId:
            messagebox.showerror("Error", "ID inválido: Debe de ser un ObjectId")
        except Exception as e:
            messagebox.showerror("Error", f"Un error ha ocurrido: {e}")



class UpdateCategoryForm(tk.Toplevel):
    def __init__(self, parent, controller, populate_common_widgets):
        super().__init__(parent)
        self.controller = controller
        self.title("Actualizar datos de categoría")
        self.geometry("600x500")

        window_msg1 = tk.Label(self, text="Ingrese el ID de la categoría a actualizar", font=("Helvetica", 16))
        window_msg1.pack(pady=10)
        
        id_label = tk.Label(self, text="ID")
        id_label.pack(pady=5)
        self.id_input = tk.Entry(self)
        self.id_input.pack(pady=5)

        window_msg2 = tk.Label(self, text="Ingrese los nuevos datos de la categoría", font=("Helvetica", 16))
        window_msg2.pack(pady=10)

        self.name_input, self.url_input, self.articles_input = populate_common_widgets(self, self.submit_category_data)

    def submit_category_data(self):
        try:
            id = self.id_input.get().strip()
            name = self.name_input.get().strip()
            url = self.url_input.get().strip()
            articles = [article.strip() for article in self.articles_input.get().split(",") if article.strip()]
            self.controller.update_category(id, name, url, articles)
            messagebox.showinfo("Exito", "Categoría actualizada correctamente!")
        except InvalidId:
            messagebox.showerror("Error", "ID inválido: Debe ser un ObjectId")
        except Exception as e:
            messagebox.showerror("Error", f"Un error ha ocurrido: {e}")


class ReplaceCategoryForm(tk.Toplevel):
    def __init__(self, parent, controller, populate_common_widgets):
        super().__init__(parent)
        self.controller = controller
        self.title("Reemplazar datos de categoría")
        self.geometry("600x500")

        window_msg1 = tk.Label(self, text="Ingrese el ID de la categoría a reemplazar", font=("Helvetica", 16))
        window_msg1.pack(pady=10)

        id_label = tk.Label(self, text="ID")
        id_label.pack(pady=5)
        self.id_input = tk.Entry(self)
        self.id_input.pack(pady=5)

        window_msg2 = tk.Label(self, text="Ingrese los nuevos datos de la categoría", font=("Helvetica", 16))
        window_msg2.pack(pady=10)

        self.name_input, self.url_input, self.articles_input = populate_common_widgets(self, self.submit_category_data)

    def submit_category_data(self):
        try:
            id = self.id_input.get().strip()
            name = self.name_input.get().strip()
            url = self.url_input.get().strip()
            articles = [article.strip() for article in self.articles_input.get().split(",") if article.strip()]
            self.controller.replace_category(id, name, url, articles)
            messagebox.showinfo("Exito", "Categoría remplazada correctamente!")
        except InvalidId:
            messagebox.showerror("Error", "ID inválido: Debe ser un ObjectId")
        except Exception as e:
            messagebox.showerror("Error", f"Un error ha ocurrido: {e}")


class DeleteCategoryForm(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.title("Eliminar Categoría")
        self.geometry("600x200")

        window_msg = tk.Label(self, text="Ingrese el ID de la categoría a eliminar", font=("Helvetica", 16))
        window_msg.pack(pady=10)

        id_label = tk.Label(self, text="ID")
        id_label.pack(pady=5)
        self.id_input = tk.Entry(self)
        self.id_input.pack(pady=5)

        submit_button = tk.Button(self, text="Eliminar", width=50, height=3, command=self.submit_category_data)
        submit_button.pack(pady=10)

    def submit_category_data(self):
        try:
            id = self.id_input.get().strip()
            self.controller.delete_category(id)
            messagebox.showinfo("Exito", "Comentario eliminado correctamente!")
        except InvalidId:
            messagebox.showerror("Error", "ID inválido: Debe de ser un ObjectId")
        except Exception as e:
            messagebox.showerror("Error", f"Un error ha ocurrido: {e}")

