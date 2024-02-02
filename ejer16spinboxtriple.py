from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import random

class Aplicacion:
    def __init__(self,ventana):
        self.label1=ttk.Label(ventana, text="R:").grid(column=0, row=0, padx=10, pady=10)
        self.spinbox1=ttk.Spinbox(ventana, from_=0, to=255, width=10)        
        self.spinbox1.set(255)        
        self.spinbox1.grid(column=1, row=0, padx=10, pady=10)
        self.spinbox1.bind("<Button>",self.cambio)

        self.label2=ttk.Label(ventana, text="G:").grid(column=0, row=1, padx=10, pady=10)
        self.spinbox2=ttk.Spinbox(ventana, from_=0, to=255, width=10)        
        self.spinbox2.set(0)        
        self.spinbox2.grid(column=1, row=1, padx=10, pady=10)
        self.spinbox2.bind("<Button>",self.cambio)

        self.label3=ttk.Label(ventana, text="B:").grid(column=0, row=2, padx=10, pady=10)
        self.spinbox3=ttk.Spinbox(ventana, from_=0, to=255, width=10)        
        self.spinbox3.set(0)        
        self.spinbox3.grid(column=1, row=2, padx=10, pady=10)
        self.spinbox3.bind("<Button>",self.cambio)
        
        self.label4=ttk.Label(ventana, text="", width=20)
        self.label4.grid(column=2, row=1, padx=10, pady=10)
        self.cambio()
    def cambio(self,*args):
        mitupla=(int(self.spinbox1.get()),int(self.spinbox2.get()),int(self.spinbox3.get()))
        self.label4.configure(text="El color compuesto")
        self.label4.configure(background=rgb_color(mitupla))

       

class App(Tk):
    def __init__(self):
        super().__init__()
        self.configure(padx=30,pady=30)
        self.title("Calculadora")
        w=425
        h=300
        x = (self.winfo_screenwidth()/2)-(w/2)
        y = (self.winfo_screenheight()/2)-(h/2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(False,False)
    
    
def rgb_color(rgb):
    return '#%02x%02x%02x' % rgb

app=App()
Aplicacion(app)
app.mainloop()