import tkinter as tk
import mysql.connector
from tkinter import ttk
import socios
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.base()
        self.contenido()
    def contenido(self):
        #EMPNO
        self.lNombre = tk.Label(self,text="Empno: ",background="#6B1234").grid(column=0,row=0)
        self.vNombre=tk.IntVar()
        self.tNombre = tk.Entry(self,textvariable=self.vNombre,width=10)
        self.tNombre.grid(column=1,row=0)
        #NOMBRE
        self.lNombre = tk.Label(self,text="Nombre: ",background="#6B1234").grid(column=0,row=1)
        self.vNombre=tk.StringVar()
        self.tNombre = tk.Entry(self,textvariable=self.vNombre,width=10)
        self.tNombre.grid(column=1,row=1)
        #APELLIDO
        self.lApellido = tk.Label(self,text="Apellido: ",background="#6B1234").grid(column=0,row=2)
        self.vApellido=tk.StringVar()
        self.tApellido = tk.Entry(self,textvariable=self.vApellido,width=10)
        self.tApellido.grid(column=1,row=2)
        #JOB
        self.lJob = tk.Label(self,text="Job: ",background="#6B1234").grid(column=0,row=3)
        self.vJob=tk.StringVar()
        self.tJob = tk.Entry(self,textvariable=self.vJob,width=10)
        self.tJob.grid(column=1,row=3)
        #MGR
        self.lMGR = tk.Label(self,text="MGR: ",background="#6B1234").grid(column=0,row=4)
        self.vMGR=tk.StringVar()
        jefes=socios.Socios.get_jefes
        self.tMGR = ttk.Combobox(self,values=jefes,textvariable=self.vMGR,state="readonly",width=10)
        self.tMGR.grid(column=1,row=4)
        #SAL
        self.lSAL= tk.Label(self,text="SAL: ",background="#6B1234").grid(column=0,row=5)
        self.vSAL=tk.DoubleVar()
        self.tSAL= ttk.Entry(self,textvariable=self.vSAL,width=10)
        self.tSAL.grid(column=1,row=5)
        #COM
        self.lCOM = tk.Label(self,text="COMM: ",background="#6B1234").grid(column=0,row=6)
        self.vCOM=tk.DoubleVar()
        self.tCOM = ttk.Entry(self,textvariable=self.vCOM,width=10)
        self.tCOM.grid(column=1,row=6)
        #DEPTNO
        self.lDEPTNO= tk.Label(self,text="DEPTNO: ",background="#6B1234").grid(column=0,row=7)
        self.vDEPTNO=tk.StringVar()
        departamentos=("BBVA","HNOS JHON","NIKE")
        self.tDEPTNO = ttk.Combobox(self,values=departamentos,textvariable=self.vDEPTNO,state="readonly",width=10)
        self.tDEPTNO.grid(column=1,row=7)
        #BOTON
        self.bAgregar=tk.Button(self,text="AGREGAR",command=self.añadir)
        self.bAgregar.grid(column=0,row=8)
    def añadir(self):
        empleado = (self.vNombre.get(),self.vApellido.get(),self.vJob.get(),self.vMGR.get(),self.vSAL.get(),self.vCOM.get(),self.vDEPTNO.get())
        print(empleado)
        self.vNombre=""
        self.vApellido=""
        self.vJob=""
        self.vMGR=""
        self.vSAL=""
        self.vCOM=""
        self.vDEPTNO=""
 
    def base(self):
        self.title("CAJERO")
        w = 300
        h = 300
        x = (self.winfo_screenwidth() / 2) - (w / 2)
        y = (self.winfo_screenheight() / 2) - (h / 2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(False, False)
        self.configure(background="#6B1234")        
app = App()
app.mainloop()