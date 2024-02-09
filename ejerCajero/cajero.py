from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb

class Aplicacion:
    def __init__(self,ventana):
        self.label1=ttk.Label(ventana, text="R:").grid(column=0, row=0, padx=10, pady=10)

class App(Tk):
    def __init__(self):
        super().__init__()
        self.configure(padx=30,pady=30)
        self.title("Cajero")
        w=425
        h=300
        x = (self.winfo_screenwidth()/2)-(w/2)
        y = (self.winfo_screenheight()/2)-(h/2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(False,False)

app=App()
Aplicacion(app)
app.mainloop()
    