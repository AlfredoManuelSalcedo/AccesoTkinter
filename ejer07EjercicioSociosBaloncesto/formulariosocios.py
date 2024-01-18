import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb 
from tkinter import scrolledtext as st 
import socio

class FormularioSocios:
    def __init__(self):
        self.socio=socio.Socio()
        self.ventana1=tk.Tk()
        self.ventana1.title("Socios de baloncesto")
        self.cuaderno1 = ttk.Notebook(self.ventana1)
        self.Insertar()
        self.consultaSocio()
        self.cuaderno1.grid(column=0, row=0, padx=10,pady=10)
        self.ventana1.mainloop()

    def Insertar(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Insertar socio")

        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Socio")
        self.labelframe1.grid(column=0,row=0,padx=5,pady=10)

        #====================socioID=====================#
        self.label1=ttk.Label(self.labelframe1, text="socioID:")
        self.label1.grid(column=0,row=0,padx=4,pady=4)

        self.socioID=tk.IntVar()
        self.entrysocioID=ttk.Entry(self.labelframe1,textvariable=self.socioID)
        self.entrysocioID.grid(column=1,row=0,padx=4,pady=4)

        #====================nombre=====================#
        self.label2=ttk.Label(self.labelframe1, text="Nombre:")
        self.label2.grid(column=0, row=1,padx=4,pady=4)

        self.nombre=tk.StringVar()
        self.entrynombre=ttk.Entry(self.labelframe1,textvariable=self.nombre)
        self.entrynombre.grid(column=1,row=1,padx=4,pady=4)

        #====================estatura=====================#
        self.label3=ttk.Label(self.labelframe1, text="Estatura:")
        self.label3.grid(column=0, row=2,padx=4,pady=4)

        self.estatura=tk.IntVar()
        self.entryestatura=ttk.Entry(self.labelframe1,textvariable=self.estatura)
        self.entryestatura.grid(column=1,row=2,padx=4,pady=4)

        #====================edad=====================#
        self.label4=ttk.Label(self.labelframe1, text="Edad:")
        self.label4.grid(column=0, row=3,padx=4,pady=4)

        self.edad=tk.IntVar()
        self.entryedad=ttk.Entry(self.labelframe1,textvariable=self.edad)
        self.entryedad.grid(column=1,row=3,padx=4,pady=4)

        #====================localidad=====================#
        self.label5=ttk.Label(self.labelframe1, text="Localidad:")
        self.label5.grid(column=0, row=4,padx=4,pady=4)

        self.localidad=tk.StringVar()
        self.entrylocalidad=ttk.Entry(self.labelframe1,textvariable=self.localidad)
        self.entrylocalidad.grid(column=1,row=4,padx=4,pady=4)

        #====================boton=====================#
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.BInsertar)
        self.boton1.grid(column=1,row=5,padx=4,pady=4)

    def BInsertar(self):
        datos=(self.socioID.get(), self.nombre.get(),self.estatura.get(),self.edad.get(),self.localidad.get())
        self.socio.nuevo_socio(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.socioID.set("")
        self.nombre.set("")
        self.estatura.set("")
        self.edad.set("")
        self.localidad.set("")

    def consultaSocio(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Consultar socio")
    

aplicacion1=FormularioSocios()

        



