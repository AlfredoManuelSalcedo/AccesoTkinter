import tkinter as tk
from tkinter import ttk

class Application(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Posicionar elementos Tcl/Tk")
        main_window.configure(width=300,height=200)

        self.button = ttk.Button(self, text="Hola, mundo!")
        self.button.place(x=60,y=40, width=100,height=30)
        self.place(relwidth=1,relheight=1)
        

#main
principal= tk.Tk()
app = Application(principal)
app.mainloop()