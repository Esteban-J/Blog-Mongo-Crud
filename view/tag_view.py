import tkinter as tk
from view.base_view import BaseView
from tkinter import messagebox
from bson.errors import InvalidId

class TagView:
    def __init__(self, root, controller):
        self.controller = controller
        self.view = BaseView(root)
        self.root = root

    def display_tag_crud(self):
        self.root.main_frame.pack_forget()
        self.view.main_frame.pack(fill="both", expand=True)

        label = tk.Label(self.view.main_frame, text="Tags", font=("Helvetica", 16))
        label.pack(pady=20)

        buttons = [
            ("Crear", lambda: self.display_tag_form(1)),
            ("Actualizar", lambda: self.display_tag_form(2)),
            ("Remplazar", lambda: self.display_tag_form(3)),
            ("Eliminar", lambda: self.display_tag_form(4)),
            ("Ver lista", lambda: self.display_tag_form(5)),
        ]

        for text, command in buttons:
            button = tk.Button(self.view.main_frame, text=text, width=50, height=3, command=command)
            button.pack(pady=10)

    def display_tag_form(self, num):
        form_classes = {
            1: CreateTagForm,
            2: UpdateTagForm,
            3: ReplaceTagForm,
            4: DeleteTagForm,
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

        url_label = tk.Label(parent, text="Url")
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


class CreateTagForm(tk.Toplevel):
    def __init__(self, parent, controller, populate_common_widgets):
        super().__init__(parent)
        self.controller = controller
        self.title("Crear Tag")
        self.geometry("600x300")

        window_msg = tk.Label(self, text="Ingrese los datos del tag", font=("Helvetica", 16))
        window_msg.pack(pady=10)

        self.name_input, self.url_input, self.articles_input = populate_common_widgets(self, self.submit_tag_data)

    def submit_tag_data(self):
        try:
            name = self.name_input.get().strip()
            url = self.url_input.get().strip()
            articles = [article.strip() for article in self.articles_input.get().split(",") if article.strip()]
            self.controller.create_tag(name, url, articles)
            messagebox.showinfo("Exito", "Tag creado correctamente!")
        except InvalidId:
            messagebox.showerror("Error", "ID inválido: Debe de ser un ObjectId")
        except Exception as e:
            messagebox.showerror("Error", f"Un error ha ocurrido: {e}")


class UpdateTagForm(tk.Toplevel):
    def __init__(self, parent, controller, populate_common_widgets):
        super().__init__(parent)
        self.controller = controller
        self.title("Actualizar datos de Tag")
        self.geometry("600x500")

        window_msg1 = tk.Label(self, text="Ingrese el ID del tag a actualizar ", font=("Helvetica", 16))
        window_msg1.pack(pady=10)

        id_label = tk.Label(self, text="Tag ID")
        id_label.pack(pady=5)
        self.id_input = tk.Entry(self)
        self.id_input.pack(pady=5)

        window_msg2 = tk.Label(self, text="Ingrese los datos del nuevo tag", font=("Helvetica", 16))
        window_msg2.pack(pady=10)

        self.name_input, self.url_input, self.articles_input = populate_common_widgets(self, self.submit_tag_data)

    def submit_tag_data(self):
        try:
            id = self.id_input.get().strip()
            name = self.name_input.get().strip()
            url = self.url_input.get().strip()
            articles = [article.strip() for article in self.articles_input.get().split(",") if article.strip()]
            self.controller.update_tag(id, name, url, articles)
            messagebox.showinfo("Exito", "Tag actualizado correctamente!")
        except InvalidId:
            messagebox.showerror("Error", "ID inválido: Debe de ser un ObjectId")
        except Exception as e:
            messagebox.showerror("Error", f"Un error ha ocurrido: {e}")


class ReplaceTagForm(tk.Toplevel):
    def __init__(self, parent, controller, populate_common_widgets):
        super().__init__(parent)
        self.controller = controller
        self.title("Remplazar datos de Tag")
        self.geometry("600x500")

        window_msg1 = tk.Label(self, text="Ingrese el ID del tag a remplazar", font=("Helvetica", 16))
        window_msg1.pack(pady=10)

        id_label = tk.Label(self, text="Tag ID")
        id_label.pack(pady=5)
        self.id_input = tk.Entry(self)
        self.id_input.pack(pady=5)

        window_msg2 = tk.Label(self, text="Ingrese los daos del nuevo Tag", font=("Helvetica", 16))
        window_msg2.pack(pady=10)

        self.name_input, self.url_input, self.articles_input = populate_common_widgets(self, self.submit_tag_data)

    def submit_tag_data(self):
        try:
            id = self.id_input.get().strip()
            name = self.name_input.get().strip()
            url = self.url_input.get().strip()
            articles = [article.strip() for article in self.articles_input.get().split(",") if article.strip()]
            self.controller.replace_tag(id, name, url, articles)
            messagebox.showinfo("Exito", "Tag remplazado correctamente!")
        except InvalidId:
            messagebox.showerror("Error", "ID inválido: Debe de ser un ObjectId")
        except Exception as e:
            messagebox.showerror("Error", f"Un error ha ocurrido: {e}")


class DeleteTagForm(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.title("Eliminar Tag")
        self.geometry("600x200")

        window_msg = tk.Label(self, text="Ingrese el ID del tag a eliminar", font=("Helvetica", 16))
        window_msg.pack(pady=10)

        id_label = tk.Label(self, text="Tag ID")
        id_label.pack(pady=5)
        self.id_input = tk.Entry(self)
        self.id_input.pack(pady=5)

        submit_button = tk.Button(self, text="Eliminar", width=50, height=3, command=self.submit_tag_data)
        submit_button.pack(pady=10)

    def submit_tag_data(self):
        try:
            id = self.id_input.get().strip()
            self.controller.delete_tag(id)
            messagebox.showinfo("Exito", "Tag eliminado correctamente!")
        except InvalidId:
            messagebox.showerror("Error", "ID inválido: Debe de ser un ObjectId")
        except Exception as e:
            messagebox.showerror("Error", f"Un error ha ocurrido: {e}")
