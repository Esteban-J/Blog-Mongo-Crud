import tkinter as tk
from view.base_view import BaseView
from tkcalendar import DateEntry
import tkinter.messagebox as messagebox
from bson.errors import InvalidId

class ArticleView:
    def __init__(self, root, controller):
        self.controller = controller
        self.view = BaseView(root)
        self.root = root

    def display_article_crud(self):
        self.root.main_frame.pack_forget()
        self.view.main_frame.pack(fill="both", expand=True)
        
        label = tk.Label(self.view.main_frame, text="Artículos", font=("Helvetica", 16))
        label.pack(pady=20)

        buttons = [
            ("Crear", lambda: self.display_article_form(1)),
            ("Actualizar", lambda: self.display_article_form(2)),
            ("Remplazar", lambda: self.display_article_form(3)),
            ("Eliminar", lambda: self.display_article_form(4)),
            ("Consultar", lambda: self.display_article_form(5)),
            ("Regresar", self.back_to_main),
        ]

        for text, command in buttons:
            button = tk.Button(self.view.main_frame, text=text, width=50, height=3, command=command)
            button.pack(pady=10)

    def display_article_form(self, num):
        form_classes = {
            1: CreateInputForm,
            2: UpdateInputForm,
            3: ReplaceInputForm,
            4: DeleteInputForm,
            5: ShowArticles
        }
        
        if num in form_classes:
            if num == 4 or num == 5:
                form_classes[num](self.view.main_frame, self.controller)
            else:
                form_classes[num](self.view.main_frame, self.controller, self.populate_common_widgets)


    def populate_common_widgets(self, parent, submit_command):
        title_label = tk.Label(parent, text="Título")
        title_label.pack(pady=5)
        title_input = tk.Entry(parent)
        title_input.pack(pady=5)

        date_label = tk.Label(parent, text="Fecha")
        date_label.pack(pady=5)
        date_input = DateEntry(parent, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern="yyyy-mm-dd")
        date_input.pack(pady=5)

        text_label = tk.Label(parent, text="Texto")
        text_label.pack(pady=5)
        text_input = tk.Entry(parent)
        text_input.pack(pady=5)

        article_id_label = tk.Label(parent, text="Id del Usuario")
        article_id_label.pack(pady=5)
        article_id_input = tk.Entry(parent)
        article_id_input.pack(pady=5)

        comments_ids_label = tk.Label(parent, text="Comentarios (IDs separados por comas)")
        comments_ids_label.pack(pady=5)
        comments_ids_input = tk.Entry(parent)
        comments_ids_input.pack(pady=5)

        tags_ids_label = tk.Label(parent, text="Tags (IDs separados por comas)")
        tags_ids_label.pack(pady=5)
        tags_ids_input = tk.Entry(parent)
        tags_ids_input.pack(pady=5)

        categories_ids_label = tk.Label(parent, text="Categorías (IDs separados por comas)")
        categories_ids_label.pack(pady=5)
        categories_ids_input = tk.Entry(parent)
        categories_ids_input.pack(pady=5)

        submit_button = tk.Button(parent, text="Enviar", width=50, height=3, command=submit_command)
        submit_button.pack(pady=10)

        return title_input, date_input, text_input, article_id_input, comments_ids_input, tags_ids_input, categories_ids_input
    
    def back_to_main(self):
        self.root.main_frame.pack(fill="both", expand=True)
        self.view.main_frame.destroy()
        self.view = BaseView(self.root)


class CreateInputForm(tk.Toplevel):
    def __init__(self, parent, controller, populate_common_widgets):
        super().__init__(parent)
        self.controller = controller
        self.title("Crear Artículo")
        self.geometry("600x600")

        window_msg = tk.Label(self, text="Ingrese los datos del artículo", font=("Helvetica", 16))
        window_msg.pack(pady=10)

        self.title_input, self.date_input, self.text_input, self.article_id_input, self.comments_ids_input, self.tags_ids_input, self.categories_ids_input = populate_common_widgets(self, self.submit_article_data)

    def submit_article_data(self):
        try:
            title = self.title_input.get().strip()
            date = self.date_input.get().strip()
            text = self.text_input.get().strip()
            article_id = self.article_id_input.get().strip() 
            comments_ids = [comment.strip() for comment in self.comments_ids_input.get().split(",") if comment.strip()]
            tags_ids = [tag.strip() for tag in self.tags_ids_input.get().split(",") if tag.strip()]
            categories_ids = [category.strip() for category in self.categories_ids_input.get().split(",") if category.strip()]
            self.controller.create_article(title, date, text, article_id, comments_ids, tags_ids, categories_ids)
            messagebox.showinfo("Exito", "Artículo creado correctamente!")
        except InvalidId as e:
            messagebox.showerror("Error", "Id invalido: El id debe de ser un ObjectId")
        except Exception as e:
            messagebox.showerror("Error", f"Un error ha ocurrido: {e}")


class UpdateInputForm(tk.Toplevel):
    def __init__(self, parent, controller, populate_common_widgets):
        super().__init__(parent)
        self.controller = controller
        self.title("Actualizar datos de artículo")
        self.geometry("600x700")

        window_msg1 = tk.Label(self, text="Ingrese el ID del artículo a actualizar", font=("Helvetica", 16))
        window_msg1.pack(pady=10)

        id_label = tk.Label(self, text="Id")
        id_label.pack(pady=5)
        self.id_input = tk.Entry(self)
        self.id_input.pack(pady=5)
        
        window_msg2 = tk.Label(self, text="Ingrese los nuevos datos del artículo", font=("Helvetica", 16))
        window_msg2.pack(pady=10)

        self.title_input, self.date_input, self.text_input, self.article_id_input, self.comments_ids_input, self.tags_ids_input, self.categories_ids_input = populate_common_widgets(self, self.submit_article_data)

    def submit_article_data(self):
        try:
            id = self.id_input.get().strip()
            title = self.title_input.get().strip()
            date = self.date_input.get().strip()
            text = self.text_input.get().strip()
            article_id = self.article_id_input.get().strip() 
            comments_ids = [comment.strip() for comment in self.comments_ids_input.get().split(",") if comment.strip()]
            tags_ids = [tag.strip() for tag in self.tags_ids_input.get().split(",") if tag.strip()]
            categories_ids = [category.strip() for category in self.categories_ids_input.get().split(",") if category.strip()]
            self.controller.update_article(id, title, date, text, article_id, comments_ids, tags_ids, categories_ids)
            messagebox.showinfo("Exito", "Artículo actualizado correctamente!")
        except InvalidId as e:
            messagebox.showerror("Error", "Id invalido: El id debe de ser un ObjectId")
        except Exception as e:
            messagebox.showerror("Error", f"Un error ha ocurrido: {e}")


class ReplaceInputForm(tk.Toplevel):
    def __init__(self, parent, controller, populate_common_widgets):
        super().__init__(parent)
        self.controller = controller
        self.title("Remplazar datos de artículo")
        self.geometry("600x700")

        window_msg1 = tk.Label(self, text="Ingrese el ID del artículo a Remplazar", font=("Helvetica", 16))
        window_msg1.pack(pady=10)

        id_label = tk.Label(self, text="Id")
        id_label.pack(pady=5)
        self.id_input = tk.Entry(self)
        self.id_input.pack(pady=5)
        
        window_msg2 = tk.Label(self, text="Ingrese los nuevos datos del artículo", font=("Helvetica", 16))
        window_msg2.pack(pady=10)

        self.title_input, self.date_input, self.text_input, self.article_id_input, self.comments_ids_input, self.tags_ids_input, self.categories_ids_input = populate_common_widgets(self, self.submit_article_data)

    def submit_article_data(self):
        try:
            id_input = self.id_input.get().strip()
            title = self.title_input.get().strip()
            date = self.date_input.get().strip()
            text = self.text_input.get().strip()
            article_id = self.article_id_input.get().strip() 
            comments_ids = [comment.strip() for comment in self.comments_ids_input.get().split(",") if comment.strip()]
            tags_ids = [tag.strip() for tag in self.tags_ids_input.get().split(",") if tag.strip()]
            categories_ids = [category.strip() for category in self.categories_ids_input.get().split(",") if category.strip()]
            self.controller.replace_article(id_input, title, date, text, article_id, comments_ids, tags_ids, categories_ids)
            messagebox.showinfo("Exito", "Artículo reemplazado correctamente!")
        except InvalidId as e:
            messagebox.showerror("Error", "Id invalido: El id debe de ser un ObjectId")
        except Exception as e:
            messagebox.showerror("Error", f"Un error ha ocurrido: {e}")


class DeleteInputForm(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.title("Eliminar artículo")
        self.geometry("600x200")

        self.window_msg = tk.Label(self, text="Ingrese el ID del artículo a eliminar", font=("Helvetica", 16))
        self.window_msg.pack(pady=10)

        self.id_label = tk.Label(self, text="ID")
        self.id_label.pack(pady=5)
        self.id_input = tk.Entry(self)
        self.id_input.pack(pady=5)

        self.submit_button = tk.Button(self, text="Eliminar", width=50, height=3, command=self.submit_article_data)
        self.submit_button.pack(pady=10)

    def submit_article_data(self):
        try:
            id = self.id_input.get()
            self.controller.delete_article(id)
            messagebox.showinfo("Exito", "Artículo eliminado correctamente!")
        except InvalidId as e:
            messagebox.showerror("Error", "Id invalido: El id debe de ser un ObjectId")
        except Exception as e:
            messagebox.showerror("Error", f"Un error ha ocurrido: {e}")

class ShowArticles(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.title("Mostrar artículos")
        self.geometry("600x400")

        search_frame = tk.Frame(self)
        search_frame.pack(pady=5)

        tk.Label(search_frame, text="ID de Artículo:").pack(side="left", padx=5)
        self.article_id_entry = tk.Entry(search_frame)
        self.article_id_entry.pack(side="left", padx=5)
        search_button = tk.Button(search_frame, text="Buscar", command=self.search_article_by_id)
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

        self.articles_per_page = 5
        self.current_page = 0

        self.articles = self.controller.get_articles()
        self.total_articles = len(self.articles)
        self.display_articles_page()


    def refresh_data(self):
        self.current_page = 0
        self.articles = self.controller.get_articles()
        self.total_articles = len(self.articles)
        self.display_articles_page()

    def search_article_by_id(self):
        article_id = self.article_id_entry.get().strip()

        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        article = next((article for article in self.articles if str(article['_id']) == article_id), None)

        if article:
            article_text = f"ID de Artículo: {article['_id']}\nTítulo: {article['title']}\nFecha: {article['date']}\nTexto: {article['text']}\nUsuario: {article['user']}\nComentarios: {article['comments']}\nTags: {article['tags']}\nCategorías: {article['categories']}"
            article_display = tk.Text(self.scrollable_frame, height=4, wrap="word")
            article_display.insert("1.0", article_text)
            article_display.configure(state="disabled")
            article_display.pack(pady=5)
        else:
            self.display_articles_page()
            messagebox.showerror("Error", "Usuario no encontrado")

        self.scrollable_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def display_articles_page(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        start_index = self.current_page * self.articles_per_page
        end_index = min(start_index + self.articles_per_page, self.total_articles)

        for i in range(start_index, end_index):
            article = self.articles[i]
            article_text = f"ID de Artículo: {article['_id']}\nTítulo: {article['title']}\nFecha: {article['date']}\nTexto: {article['text']}\nUsuario: {article['user']}\nComentarios: {article['comments']}\nTags: {article['tags']}\nCategorías: {article['categories']}"
            article_display = tk.Text(self.scrollable_frame, height=6, wrap="word")
            article_display.insert("1.0", article_text)
            article_display.configure(state="disabled")
            article_display.pack(pady=5, fill="both", expand=True)

        self.scrollable_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        self.create_pagination_buttons()

    def create_pagination_buttons(self):
        for widget in self.pagination_frame.winfo_children():
            widget.destroy()

        if self.current_page > 0:
            prev_button = tk.Button(self.pagination_frame, text="Previous", command=self.prev_page)
            prev_button.pack(side="left", padx=10)

        if self.current_page < (self.total_articles // self.articles_per_page):
            next_button = tk.Button(self.pagination_frame, text="Next", command=self.next_page)
            next_button.pack(side="left", padx=10)

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.display_articles_page()

    def next_page(self):
        if (self.current_page + 1) * self.articles_per_page < self.total_articles:
            self.current_page += 1
            self.display_articles_page()

    


