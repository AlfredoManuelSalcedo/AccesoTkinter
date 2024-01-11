import tkinter as tk
from tkinter import ttk

class Application(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Posicionar elementos Tcl/Tk")
        main_window.configure(width=300,height=200)

#main
principal= tk.Tk()
app = Application(principal)
app.mainloop()