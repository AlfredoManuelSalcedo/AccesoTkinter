from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import bbdd
lista_monedas=[0.01 ,0.02 ,0.05
                   ,0.10 ,0.20 ,0.50
                   ,1.00 ,2.00 ,5.00
                   ,10.00 ,20.00 ,50.00
                   ,100.00 ,200.00 ,500.00]

class Aplicacion:
    def __init__(self,ventana):
        bbdd.base.verificar()
        bbdd.base.verificartbl()
        bbdd.base.labels(ventana)
        #bbdd.base.selects(ventana)
        pos=1
        for moneda in lista_monedas:
            spinbox(ventana, pos,moneda)
            pos+=1

class spinbox:
    def __init__(self,ventana,posicion,moneda):
        self.posicion=posicion
        self.moneda=moneda
        print(moneda)
        ttk.Spinbox(ventana, from_=0, to=2000, width=5).grid(row=posicion, column=1)
        


    
    
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
    