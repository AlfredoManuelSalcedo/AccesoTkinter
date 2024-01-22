import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb 
import convertir as cv

class Aplicacion:
    def __init__(self,ventana1):
        s = ttk.Style()
        s.theme_use("default")
        s.configure("TLabelframe", background="grey")
        s.configure("TLabelframe.Label", background="grey", foreground="white", font=("verdana", 20, "bold"))
        s.configure("TButton", background="grey", foreground="white", font=("verdana", 15, "bold"))
    
        caracteristicas = {"justify":"left", "background":"#FFFFFF", "foreground":"black", "font":("Verdana", 10, "bold"), "width":20}
        caracteristicas2 = {"justify":"right", "background":"#FFFFFF", "foreground":"black", "font":("Verdana", 10, "bold"), "width":10}
        caracteristicas3 = {"width":3}

        self.lf1=ttk.LabelFrame(ventana1, text="Conversiones", labelanchor="nw")
        self.lf1.grid(column=0,row=0,padx=20,pady=10)

        
        ttk.Label(self.lf1, text="Celsius:",**caracteristicas).grid(column=0,row=0,padx=20,pady=20)
        ttk.Label(self.lf1, text="Kelvin:",**caracteristicas).grid(column=0,row=1,pady=20)
        ttk.Label(self.lf1, text="Farhenheit:",**caracteristicas).grid(column=0,row=2,pady=20)

        ttk.Button(self.lf1,text="+1",command=lambda *_: self.cambio(*_,v1="gc",v2=1),**caracteristicas3).grid(column=2,row=0, padx=10)
        ttk.Button(self.lf1,text="-1",command=lambda *_: self.cambio(*_,v1="gc",v2=-1),**caracteristicas3).grid(column=3,row=0)

        ttk.Button(self.lf1,text="+1",command=lambda *_: self.cambio(*_,v1="gf",v2=1),**caracteristicas3).grid(column=2,row=1)
        ttk.Button(self.lf1,text="-1",command=lambda *_: self.cambio(*_,v1="gf",v2=-1),**caracteristicas3).grid(column=3,row=1)

        ttk.Button(self.lf1,text="+1",command=lambda *_: self.cambio(*_,v1="gk",v2=1),**caracteristicas3).grid(column=2,row=2)
        ttk.Button(self.lf1,text="-1",command=lambda *_: self.cambio(*_,v1="gk",v2=-1),**caracteristicas3).grid(column=3,row=2)

        self.gc = tk.DoubleVar()
        caja1=ttk.Entry(self.lf1,textvariable=self.gc,**caracteristicas2)
        caja1.grid(column=1,row=0)
        caja1.bind("<Return>", lambda *_,: self.cambio(*_,v1="gc",v2=0))
        caja1.bind("<FocusOut>", lambda *_,: self.cambio(*_,v1="gc",v2=0))

        self.gf = tk.DoubleVar()
        caja2=ttk.Entry(self.lf1,textvariable=self.gf,**caracteristicas2)
        caja2.grid(column=1,row=1)
        caja2.bind("<Return>", lambda *_,: self.cambio(*_,v1="gf",v2=0))
        caja2.bind("<FocusOut>", lambda *_,: self.cambio(*_,v1="gf",v2=0))

        self.gk = tk.DoubleVar()
        caja3=ttk.Entry(self.lf1,textvariable=self.gk,**caracteristicas2)
        caja3.grid(column=1,row=2)
        caja3.bind("<Return>", lambda *_,: self.cambio(*_,v1="gk",v2=0))
        caja3.bind("<FocusOut>", lambda *_,: self.cambio(*_,v1="gk",v2=0))

        caja1.focus()
        caja1.select_range(0,tk.END)

    def cambio(self,*args,v1,v2):
        match v1:
            case "gc":
                gc=self.gc.get()+v2
                gf=cv.Convertir.c_a_f(gc,False)
                gk=cv.Convertir.c_a_k(gc,False)
            case "gf":
                gf=self.gf.get()+v2
                gc=cv.Convertir.f_a_c(gf,False)
                gk=cv.Convertir.f_a_k(gf,False)
            case "gk":
                gk=self.gk.get()+v2
                gc=cv.Convertir.k_a_c(gk,False)
                gf=cv.Convertir.k_a_f(gk,False)

        self.gc.set(gc)
        self.gf.set(gf)
        self.gk.set(gk)


        

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
    