import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb


class Aplicacion(Tk):
    def __init__(self):
        super().__init__()
        self.iniciar()
        self.labels()

    def labels(self):
        ttk.Label(self,text="EMPNO").grid(row=0,column=0,padx=5,pady=5)
        ttk.Label(self,text="ENAME").grid(row=0,column=1,padx=5,pady=5)
        ttk.Label(self,text="MGR").grid(row=0,column=2,padx=5,pady=5)
        ttk.Label(self,text="SAL").grid(row=0,column=3,padx=5,pady=5)
        ttk.Label(self,text="COMM").grid(row=0,column=4,padx=5,pady=5)
        ttk.Label(self,text="DEPTNO").grid(row=0,column=5,padx=5,pady=5)
        ttk.Label(self,text="HIREDATE").grid(row=0,column=6,padx=5,pady=5)
    
    def iniciar(self):
        self.configure(padx=30,pady=30)
        self.title("BBDD_SCOTT")
        w=800
        h=600
        x = (self.winfo_screenwidth()/2)-(w/2)
        y = (self.winfo_screenheight()/2)-(h/2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(False,False)
        self.configure(background="#4bdddb")
        

if __name__ == "__main__":
    ap=Aplicacion()
    ap.mainloop()