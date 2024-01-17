import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1-title("Prueba del control de Notebook")
        self.cuaderno1 = ttk.Notebook(self.ventana1)

        