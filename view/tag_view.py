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
            ("Consultar", lambda: self.display_tag_form(5)),
            ("Regresar", self.back_to_main),
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
            5: ShowTags
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
    
    def back_to_main(self):
        self.root.main_frame.pack(fill="both", expand=True)
        self.view.main_frame.destroy()
        self.view = BaseView(self.root)


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

class ShowTags(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.title("Mostrar Tags")
        self.geometry("600x400")

        search_frame = tk.Frame(self)
        search_frame.pack(pady=5)

        tk.Label(search_frame, text="ID del Tag:").pack(side="left", padx=5)
        self.tag_id_entry = tk.Entry(search_frame)
        self.tag_id_entry.pack(side="left", padx=5)
        search_button = tk.Button(search_frame, text="Buscar", command=self.search_tag_by_id)
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

        self.tags_per_page = 5 
        self.current_page = 0

        self.tags = self.controller.get_tags()
        self.total_tags = len(self.tags)
        self.display_tags_page()

    def refresh_data(self):
        self.current_page = 0
        self.tags = self.controller.get_tags()
        self.total_tags = len(self.tags)
        self.display_tags_page()

    def search_tag_by_id(self):
        tag_id = self.tag_id_entry.get().strip()

        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        tag = next((tag for tag in self.tags if str(tag['_id']) == tag_id), None)

        if tag:
            tag_text = f"ID del Tag: {tag['_id']}\nNombre: {tag['name']}\nurl: {tag['url']}\nArtículos: {tag['articles']}"
            tag_display = tk.Text(self.scrollable_frame, height=4, wrap="word")
            tag_display.insert("1.0", tag_text)
            tag_display.configure(state="disabled")
            tag_display.pack(pady=5)
        else:
            self.display_tags_page()
            messagebox.showerror("Error", "Tag no encontrado")

        self.scrollable_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def display_tags_page(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        start_index = self.current_page * self.tags_per_page
        end_index = min(start_index + self.tags_per_page, self.total_tags)

        for i in range(start_index, end_index):
            tag = self.tags[i]
            tag_text = f"ID de Usuario: {tag['_id']}\nNombre: {tag['name']}\nurl: {tag['url']}\nArtículos: {tag['articles']}"
            tag_display = tk.Text(self.scrollable_frame, height=6, wrap="word")
            tag_display.insert("1.0", tag_text)
            tag_display.configure(state="disabled")
            tag_display.pack(pady=5, fill="both", expand=True)

        self.scrollable_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        self.create_pagination_buttons()

    def create_pagination_buttons(self):
        for widget in self.pagination_frame.winfo_children():
            widget.destroy()

        if self.current_page > 0:
            prev_button = tk.Button(self.pagination_frame, text="Previous", command=self.prev_page)
            prev_button.pack(side="left", padx=10)

        if self.current_page < (self.total_tags // self.tags_per_page):
            next_button = tk.Button(self.pagination_frame, text="Next", command=self.next_page)
            next_button.pack(side="left", padx=10)

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.display_tags_page()

    def next_page(self):
        if (self.current_page + 1) * self.tags_per_page < self.total_tags:
            self.current_page += 1
            self.display_tags_page()