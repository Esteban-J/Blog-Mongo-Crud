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
            ("Consultar", lambda: self.display_category_form(5)),
            ("Regresar", self.back_to_main),
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
            5: ShowCategories
        }
        
        if num in form_classes:
            if num == 4 or num == 5:
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
    
    def back_to_main(self):
        self.root.main_frame.pack(fill="both", expand=True)
        self.view.main_frame.destroy()
        self.view = BaseView(self.root)


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
    
class ShowCategories(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.title("Mostrar categorías")
        self.geometry("600x400")

        search_frame = tk.Frame(self)
        search_frame.pack(pady=5)

        tk.Label(search_frame, text="ID de la categoría:").pack(side="left", padx=5)
        self.category_id_entry = tk.Entry(search_frame)
        self.category_id_entry.pack(side="left", padx=5)
        search_button = tk.Button(search_frame, text="Buscar", command=self.search_category_by_id)
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

        self.categories_per_page = 5 
        self.current_page = 0

        self.categories = self.controller.get_categories()
        self.total_categories = len(self.categories)
        self.display_categories_page()

    def refresh_data(self):
        self.current_page = 0
        self.categories = self.controller.get_categories()
        self.total_categories = len(self.categories)
        self.display_categories_page()

    def search_category_by_id(self):
        category_id = self.category_id_entry.get().strip()

        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        category = next((category for category in self.categories if str(category['_id']) == category_id), None)

        if category:
            category_text = f"ID del category: {category['_id']}\nNombre: {category['name']}\nurl: {category['url']}\nArtículos: {category['articles']}"
            category_display = tk.Text(self.scrollable_frame, height=4, wrap="word")
            category_display.insert("1.0", category_text)
            category_display.configure(state="disabled")
            category_display.pack(pady=5)
        else:
            self.display_categories_page()
            messagebox.showerror("Error", "Comentario no encontrado")

        self.scrollable_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def display_categories_page(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        start_index = self.current_page * self.categories_per_page
        end_index = min(start_index + self.categories_per_page, self.total_categories)

        for i in range(start_index, end_index):
            category = self.categories[i]
            category_text = f"ID de Usuario: {category['_id']}\nNombre: {category['name']}\nurl: {category['url']}\nArtículos: {category['articles']}"
            category_display = tk.Text(self.scrollable_frame, height=6, wrap="word")
            category_display.insert("1.0", category_text)
            category_display.configure(state="disabled")
            category_display.pack(pady=5, fill="both", expand=True)

        self.scrollable_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        self.create_pagination_buttons()

    def create_pagination_buttons(self):
        for widget in self.pagination_frame.winfo_children():
            widget.destroy()

        if self.current_page > 0:
            prev_button = tk.Button(self.pagination_frame, text="Previous", command=self.prev_page)
            prev_button.pack(side="left", padx=10)

        if self.current_page < (self.total_categories // self.categories_per_page):
            next_button = tk.Button(self.pagination_frame, text="Next", command=self.next_page)
            next_button.pack(side="left", padx=10)

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.display_categories_page()

    def next_page(self):
        if (self.current_page + 1) * self.categories_per_page < self.total_categories:
            self.current_page += 1
            self.display_categories_page()

