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

        buttons = [
            ("Crear", 1),
            ("Actualizar", 2),
            ("Remplazar", 3),
            ("Eliminar", 4),
            ("Ver lista", 5),
        ]

        for text, num in buttons:
            button = tk.Button(self.view.main_frame, text=text, width=50, height=3,
                               command=lambda num=num: self.display_user_form(num))
            button.pack(pady=10)

    def display_user_form(self, num):
        forms = {
            1: CreateFormInput,
            2: UpdateFormInput,
            3: ReplaceFormInput,
            4: DeleteFormInput,
        }
        form_class = forms.get(num)
        if form_class:
            form_class(self.view.main_frame, self.controller)

class BaseFormInput(tk.Toplevel):
    def __init__(self, parent, controller, title, fields, submit_callback):
        super().__init__(parent)
        self.controller = controller
        self.submit_callback = submit_callback
        self.title(title)
        self.geometry("600x400")

        self.inputs = {}  # Dictionary to hold input fields by name

        for field_name, field_label in fields:
            label = tk.Label(self, text=field_label)
            label.pack(pady=5)
            entry = tk.Entry(self)
            entry.pack(pady=5)
            self.inputs[field_name] = entry  # Store entry widget

        submit_button = tk.Button(self, text="Enviar", width=50, height=3, command=self.submit_user_data)
        submit_button.pack(pady=10)

    def submit_user_data(self):
        data = {name: entry.get() for name, entry in self.inputs.items()}
        # Split article/comment fields by commas if present
        if 'articles' in data:
            data['articles'] = [article.strip() for article in data['articles'].split(",") if article.strip()]
        if 'comments' in data:
            data['comments'] = [comment.strip() for comment in data['comments'].split(",") if comment.strip()]
        self.submit_callback(data)

class CreateFormInput(BaseFormInput):
    def __init__(self, parent, controller):
        fields = [
            ('name', 'Nombre'),
            ('email', 'Email'),
            ('articles', 'Artículos (IDs separados por comas)'),
            ('comments', 'Comentarios (IDs separados por comas)'),
        ]
        super().__init__(parent, controller, title="Datos nuevo usuario",
                         fields=fields, submit_callback=self.create_user)

    def create_user(self, data):
        self.controller.create_user(data['name'], data['email'], data['articles'], data['comments'])

class UpdateFormInput(BaseFormInput):
    def __init__(self, parent, controller):
        fields = [
            ('id', 'Id'),
            ('name', 'Nombre'),
            ('email', 'Email'),
            ('articles', 'Artículos (IDs separados por comas)'),
            ('comments', 'Comentarios (IDs separados por comas)'),
        ]
        super().__init__(parent, controller, title="Actualizar datos de usuario",
                         fields=fields, submit_callback=self.update_user)

    def update_user(self, data):
        self.controller.update_user(data['id'], data['name'], data['email'], data['articles'], data['comments'])

class ReplaceFormInput(BaseFormInput):
    def __init__(self, parent, controller):
        fields = [
            ('id', 'Id'),
            ('name', 'Nombre'),
            ('email', 'Email'),
            ('articles', 'Artículos (IDs separados por comas)'),
            ('comments', 'Comentarios (IDs separados por comas)'),
        ]
        super().__init__(parent, controller, title="Remplazar usuario",
                         fields=fields, submit_callback=self.replace_user)

    def replace_user(self, data):
        self.controller.replace_user(data['id'], data['name'], data['email'], data['articles'], data['comments'])

class DeleteFormInput(BaseFormInput):
    def __init__(self, parent, controller):
        fields = [
            ('id', 'Id'),
        ]
        super().__init__(parent, controller, title="Eliminar usuario",
                         fields=fields, submit_callback=self.delete_user)

    def delete_user(self, data):
        self.controller.delete_user(data['id'])
