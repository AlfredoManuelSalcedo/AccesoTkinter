import tkinter as tk
from tkinter import ttk

class Application(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Posicionar elementos en Tcl/Tk")
        main_window.columnconfigure(0, weight=1)
        main_window.rowconfigure(0, weight=1)

        self.label1 = tk.Label(
        self, text="¡Hola, mundo!", bg="#FFA500")
        self.label1.grid(row=0, column=0, sticky="nsew")

        self.label2 = tk.Label(
        self, text="¡Hola, mundo!", bg="#1E90FF")
        self.label2.grid(row=1, column=0, sticky="nsew")

        self.grid(sticky="nsew")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=5)
        self.rowconfigure(1, weight=1)

#main
principal= tk.Tk()
app = Application(principal)
app.mainloop()