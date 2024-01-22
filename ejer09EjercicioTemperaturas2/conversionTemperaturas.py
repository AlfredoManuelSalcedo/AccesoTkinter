import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb 
import convertir as cv

class Aplicacion:
    def __init__(self,ventana1):
        s =ttk.Style()
        s.configure("TLabelframe", background="grey")
        s.configure("TLabelframe.Label",background="grey", foreground="white", font=("verdana",20,"bold"))
        s.configure("TButton", background="grey",foreground="white",font=("verdana",15,"bold"))

        caracteristicas = {"justify":"left", "background":"FFFFFF","foreground":"black","font":("Verdana",10,"bold"),"width":20}
        caracteristicas2 = {"justify":"right", "background":"#FFFFFF", "foreground":"black", "font":("Verdana", 10, "bold"), "width":10}
        caracteristicas3 = {"width":3}

        self.lf1=ttk.LabelFrame(ventana1, text="Conversiones", labelanchor="nw")
        self.lf1.grid(column=0,row=0,padx=125,pady=10)

        
        ttk.Label(self.lf1, text="Celsius:",**caracteristicas).grid(column=0,row=0,padx=20,pady=20)
        ttk.Label(self.lf1, text="Kelvin:",**caracteristicas).grid(column=0,row=1,pady=20)
        ttk.Label(self.lf1, text="Farhenheit:",**caracteristicas).grid(column=0,row=2,pady=20)

        ttk.Button(self.lf1,text="+1",command=lambda *_: self.cambio(*_,v1="gc",v2=1),**caracteristicas).grid(column=2,row=0, padx=10)
        ttk.Button(self.lf1,text="-1",command=lambda *_: self.cambio(*_,v1="gc",v2=-1),**caracteristicas).grid(column=3,row=0)

        ttk.Button(self.lf1,text="+1",command=lambda *_: self.cambio(*_,v1="gf",v2=1),**caracteristicas).grid(column=2,row=1, padx=10)
        ttk.Button(self.lf1,text="-1",command=lambda *_: self.cambio(*_,v1="gf",v2=-1),**caracteristicas).grid(column=3,row=1)

        ttk.Button(self.lf1,text="+1",command=lambda *_: self.cambio(*_,v1="gk",v2=1),**caracteristicas).grid(column=2,row=2, padx=10)
        ttk.Button(self.lf1,text="-1",command=lambda *_: self.cambio(*_,v1="gk",v2=-1),**caracteristicas).grid(column=3,row=2)


        self.gc = tk.DoubleVar()
        
        

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(padx=30,pady=30)
        self.title("Conversor Temperaturas")
        w=575
        h=300
        x=(self.winfo_screenwidth()/2)-(h/2)
        y=(self.winfo_screenheight()/2)-(h/2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(False,False)
    
if __name__=="__main__":
    ap = App()
    Aplicacion(ap)
    ap.mainloop()
    