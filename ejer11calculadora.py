import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self,ventana1):

        ttk.Label(ventana1, text="Numero 1: ").grid(row=0, column=0)
        
        self.num1=tk.DoubleVar()
        self.entry1=ttk.Entry(ventana1,width=10,textvariable=self.num1)
        self.entry1.bind("<Return>", self.Calcular)
        self.entry1.bind("<FocusOut>", self.Calcular)
        self.entry1.grid(column=1,row=0)

        ttk.Label(ventana1, text=" ").grid(row=1, column=0)

        ttk.Label(ventana1, text="Operador: ").grid(row=2, column=0)
        self.operacion=tk.StringVar()
        operaciones=("+","-","*","/")
        self.combobox1=ttk.Combobox(ventana1, width=10,textvariable=self.operacion,values=operaciones,state='readonly')
        try:
            n=operaciones.index("+")
        except:
            n=0
        self.combobox1.current(n)
        self.combobox1.grid(row=2,column=1)
        self.combobox1.bind("<<ComboboxSelected>>", self.Calcular)
        
        
        ttk.Label(ventana1, text=" ").grid(row=3, column=0)

        ttk.Label(ventana1, text="Numero 2: ").grid(row=4, column=0)
        self.num2=tk.DoubleVar()
        self.entry2=ttk.Entry(ventana1,width=10,textvariable=self.num2)
        self.entry2.bind("<Return>", self.Calcular)
        self.entry2.bind("<FocusOut>", self.Calcular)
        self.entry2.grid(column=1,row=4)

        ttk.Label(ventana1, text=" ").grid(row=5, column=0)

        self.boton1=tk.Button(ventana1,text="Calcular", command=self.Calcular)
        self.boton1.grid(column=0,row=6)

        self.labelResul=ttk.Label(ventana1)
        self.labelResul.grid(column=1,row=6)

        ap.mainloop()

    def Calcular(self, *args):
        resultado=eval(str(self.num1.get())+self.combobox1.get()+str(self.num2.get()))
        self.labelResul.config(text=str(self.num1.get())+self.combobox1.get()+str(self.num2.get())+"="+str(resultado))
        

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        w=200
        h=200
        x = (self.winfo_screenwidth()/2)-(w/2)
        y = (self.winfo_screenheight()/2)-(h/2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(False,False)

if __name__ == "__main__":
    ap=App()
    Aplicacion(ap)
    