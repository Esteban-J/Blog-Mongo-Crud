import tkinter as tk

class BaseView:
    def __init__(self, root):
        self.root = root
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill="both", expand=True)

    def clear_window(root):
        # Only destroy child widgets without repacking main_frame
        for widget in root.main_frame.winfo_children():
            widget.destroy()

