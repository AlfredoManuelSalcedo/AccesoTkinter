from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import bbdd

class Aplicacion:
    def __init__(self,ventana):
        bbdd.base.verificar()
        bbdd.base.verificartbl()
        bbdd.base.labels(ventana)
        bbdd.base.selects(ventana)
    
    


class App(Tk):
    def __init__(self):
        super().__init__()
        self.configure(padx=30,pady=30)
        self.title("Cajero")
        w=425
        h=700
        x = (self.winfo_screenwidth()/2)-(w/2)
        y = (self.winfo_screenheight()/2)-(h/2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(False,False)
        self.configure(background="#e3d4ac")

app=App()
Aplicacion(app)
app.mainloop()
    