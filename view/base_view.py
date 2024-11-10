import tkinter as tk

class BaseView:
    def __init__(self, root):
        self.root = root
        self.main_frame = tk.Frame(root)
        #self.main_frame.pack(fill="both", expand=True)

