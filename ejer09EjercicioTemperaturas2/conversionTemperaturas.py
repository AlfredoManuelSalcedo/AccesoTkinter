import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb 
import convertir as cv

class Aplicacion(ventana1):
    s =ttk.Style()
    s.configure("TLabelframe", background="grey")
    s.configure("TLabelframe.Label",background="grey", foreground="white", font=("verdana",20,"bold"))
    s.configure("TButton", background="grey",foreground="white",font=("verdana",15,"bold"))

    caracteristicas = {"justify":"left", "background":"FFFFFF","foreground":"black","font":("Verdana",10,"bold"),"width":20}
    caracteristicas2 = {"justify":"right", "background":"#FFFFFF", "foreground":"black", "font":("Verdana", 10, "bold"), "width":10}
    caracteristicas3 = {"width":3}





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
    ap.mainloop()
    aplicacion=Aplicacion(ap)