import tkinter as tk
from view.base_view import BaseView
import tkinter.messagebox as messagebox
from bson.errors import InvalidId

class UserView:
    def __init__(self, root, controller):
        self.controller = controller
        self.view = BaseView(root)
        self.root = root

    def display_user_crud(self):
        self.root.main_frame.pack_forget()
        self.view.main_frame.pack(fill="both", expand=True)

        label = tk.Label(self.view.main_frame, text="Usuarios", font=("Helvetica", 16))
        label.pack(pady=20)

        self.buttons = [
            ("Crear", lambda: self.display_user_form(1)),
            ("Actualizar", lambda: self.display_user_form(2)),
            ("Remplazar", lambda: self.display_user_form(3)),
            ("Eliminar", lambda: self.display_user_form(4)),
            ("Consultar", lambda: self.display_user_form(5)),
            ("Regresar", self.back_to_main),
            
        ]

        for text, command in self.buttons:
            button = tk.Button(self.view.main_frame, text=text, width=50, height=3, command=command)
            button.pack(pady=10)

    def display_user_form(self, num):
        form_classes = {
            1: CreateUserForm,
            2: UpdateUserForm,
            3: ReplaceUserForm,
            4: DeleteUserForm,
            5: ShowUsers
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

        email_label = tk.Label(parent, text="Email")
        email_label.pack(pady=5)
        email_input = tk.Entry(parent)
        email_input.pack(pady=5)

        articles_ids_label = tk.Label(parent, text="Artículos (IDs separados por comas)")
        articles_ids_label.pack(pady=5)
        articles_ids_input = tk.Entry(parent)
        articles_ids_input.pack(pady=5)

        comments_ids_label = tk.Label(parent, text="Comentarios (IDs separados por comas)")
        comments_ids_label.pack(pady=5)
        comments_ids_input = tk.Entry(parent)
        comments_ids_input.pack(pady=5)

        submit_button = tk.Button(parent, text="Enviar", width=50, height=3, command=submit_command)
        submit_button.pack(pady=10)

        return name_input, email_input, articles_ids_input, comments_ids_input

    def back_to_main(self):
        self.root.main_frame.pack(fill="both", expand=True)
        self.view.main_frame.destroy()
        self.view = BaseView(self.root)
    
class CreateUserForm(tk.Toplevel):
    def __init__(self, parent, controller, populate_common_widgets):
        super().__init__(parent)
        self.controller = controller
        self.title("Crear Usuario")
        self.geometry("600x400")

        window_msg = tk.Label(self, text="Ingrese los datos del usuario", font=("Helvetica", 16))
        window_msg.pack(pady=10)

        self.name_input, self.email_input, self.articles_ids_input, self.comments_ids_input = populate_common_widgets(self, self.submit_user_data)

    def submit_user_data(self):
        try:
            name = self.name_input.get().strip()
            email = self.email_input.get().strip()
            articles_ids = [article.strip() for article in self.articles_ids_input.get().split(",") if article.strip()]
            comments_ids = [comment.strip() for comment in self.comments_ids_input.get().split(",") if comment.strip()]
            self.controller.create_user(name, email, articles_ids, comments_ids)
            messagebox.showinfo("Exito", "Usuario creado correctamente!")
        except InvalidId as e:
            messagebox.showerror("Error", "ID inválido: Debe ser un ObjectId")
        except Exception as e:
            messagebox.showerror("Error", f"Un error ha ocurrido: {e}")


class UpdateUserForm(tk.Toplevel):
    def __init__(self, parent, controller, populate_common_widgets):
        super().__init__(parent)
        self.controller = controller
        self.title("Actualizar datos de usuario")
        self.geometry("600x500")

        window_msg1 = tk.Label(self, text="Ingrese el ID del usuario a actualizar", font=("Helvetica", 16))
        window_msg1.pack(pady=10)

        id_label = tk.Label(self, text="Id")
        id_label.pack(pady=5)
        self.id_input = tk.Entry(self)
        self.id_input.pack(pady=5)
        
        window_msg2 = tk.Label(self, text="Ingrese los nuevos datos del usuario", font=("Helvetica", 16))
        window_msg2.pack(pady=10)

        self.name_input, self.email_input, self.articles_ids_input, self.comments_ids_input = populate_common_widgets(self, self.submit_user_data)

    def submit_user_data(self):
        try:
            user_id = self.id_input.get().strip()
            name = self.name_input.get().strip()
            email = self.email_input.get().strip()
            articles_ids = [article.strip() for article in self.articles_ids_input.get().split(",") if article.strip()]
            comments_ids = [comment.strip() for comment in self.comments_ids_input.get().split(",") if comment.strip()]
            self.controller.update_user(user_id, name, email, articles_ids, comments_ids)
            messagebox.showinfo("Exito", "Usuario actualizado correctamente!")
        except InvalidId as e:
            messagebox.showerror("Error", "ID inválido: Debe ser un ObjectId")
        except Exception as e:
            messagebox.showerror("Error", f"Un error ha ocurrido: {e}")


class ReplaceUserForm(tk.Toplevel):
    def __init__(self, parent, controller, populate_common_widgets):
        super().__init__(parent)
        self.controller = controller
        self.title("Remplazar datos de usuario")
        self.geometry("600x500")

        window_msg1 = tk.Label(self, text="Ingrese el ID del usuario a remplazar", font=("Helvetica", 16))
        window_msg1.pack(pady=10)

        id_label = tk.Label(self, text="Id")
        id_label.pack(pady=5)
        self.id_input = tk.Entry(self)
        self.id_input.pack(pady=5)
        
        window_msg2 = tk.Label(self, text="Ingrese los nuevos datos del usuario", font=("Helvetica", 16))
        window_msg2.pack(pady=10)

        self.name_input, self.email_input, self.articles_ids_input, self.comments_ids_input = populate_common_widgets(self, self.submit_user_data)

    def submit_user_data(self):
        try:
            user_id = self.id_input.get().strip()
            name = self.name_input.get().strip()
            email = self.email_input.get().strip()
            articles_ids = [article.strip() for article in self.articles_ids_input.get().split(",") if article.strip()]
            comments_ids = [comment.strip() for comment in self.comments_ids_input.get().split(",") if comment.strip()]
            self.controller.replace_user(user_id, name, email, articles_ids, comments_ids)
            messagebox.showinfo("Exito", "Usuario reemplazado correctamente!")
        except InvalidId as e:
            messagebox.showerror("Error", "ID inválido:  Debe ser un ObjectId")
        except Exception as e:
            messagebox.showerror("Error", f"Un error ha ocurrido: {e}")


class DeleteUserForm(tk.Toplevel):
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
        try:
            user_id = self.id_input.get().strip()
            self.controller.delete_user(user_id)
            messagebox.showinfo("Exito", "Usuario eliminado correctamente!")
        except InvalidId as e:
            messagebox.showerror("Error", "Id invalido: El id debe de ser un ObjectId")
        except Exception as e:
            messagebox.showerror("Error", f"Un error ha ocurrido: {e}")


class ShowUsers(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.title("Mostrar usuarios")
        self.geometry("600x400")

        # Search functionality
        search_frame = tk.Frame(self)
        search_frame.pack(pady=5)

        tk.Label(search_frame, text="ID de Usuario:").pack(side="left", padx=5)
        self.user_id_entry = tk.Entry(search_frame)
        self.user_id_entry.pack(side="left", padx=5)
        search_button = tk.Button(search_frame, text="Buscar", command=self.search_user_by_id)
        search_button.pack(side="left", padx=5)

        # Refresh button
        refresh_button = tk.Button(self, text="Refrescar", command=self.refresh_data)
        refresh_button.pack(pady=5)

        # Set up scrollable canvas
        self.canvas = tk.Canvas(self)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create a frame to hold the user data (this frame will scroll)
        self.scrollable_frame = tk.Frame(self.canvas)
        
        # Create a window in the canvas to hold the scrollable frame
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="top", fill="both", expand=True)

        # Pagination frame (outside the scrollable frame)
        self.pagination_frame = tk.Frame(self)
        self.pagination_frame.pack(pady=5)

        # Pagination variables
        self.users_per_page = 5  # Number of users per page
        self.current_page = 0

        # Retrieve the users and display them
        self.users = self.controller.get_users()  # assuming this returns a list of users
        self.total_users = len(self.users)
        self.display_users_page()


    def refresh_data(self):
        """Refresh the user data from the controller and update the display."""
        self.current_page = 0
        self.users = self.controller.get_users()
        self.total_users = len(self.users)
        self.display_users_page()

    def search_user_by_id(self):
        user_id = self.user_id_entry.get().strip()

        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        user = next((user for user in self.users if str(user['_id']) == user_id), None)

        if user:
            user_text = f"ID de Usuario: {user['_id']}\nNombre: {user['name']}\nEmail: {user['email']}\nArtículos: {user['articles']}\nComentarios: {user['comments']}"
            user_display = tk.Text(self.scrollable_frame, height=4, wrap="word")
            user_display.insert("1.0", user_text)
            user_display.configure(state="disabled")
            user_display.pack(pady=5)
        else:
            self.display_users_page()
            messagebox.showerror("Error", "Usuario no encontrado")

        self.scrollable_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def display_users_page(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        start_index = self.current_page * self.users_per_page
        end_index = min(start_index + self.users_per_page, self.total_users)

        for i in range(start_index, end_index):
            user = self.users[i]
            user_text = f"ID de Usuario: {user['_id']}\nNombre: {user['name']}\nEmail: {user['email']}\nArtículos: {user['articles']}\nComentarios: {user['comments']}"
            user_display = tk.Text(self.scrollable_frame, height=6, wrap="word")
            user_display.insert("1.0", user_text)
            user_display.configure(state="disabled")
            user_display.pack(pady=5, fill="both", expand=True)

        self.scrollable_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        self.create_pagination_buttons()

    def create_pagination_buttons(self):
        for widget in self.pagination_frame.winfo_children():
            widget.destroy()

        if self.current_page > 0:
            prev_button = tk.Button(self.pagination_frame, text="Previous", command=self.prev_page)
            prev_button.pack(side="left", padx=10)

        if self.current_page < (self.total_users // self.users_per_page):
            next_button = tk.Button(self.pagination_frame, text="Next", command=self.next_page)
            next_button.pack(side="left", padx=10)

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.display_users_page()

    def next_page(self):
        if (self.current_page + 1) * self.users_per_page < self.total_users:
            self.current_page += 1
            self.display_users_page()

    

