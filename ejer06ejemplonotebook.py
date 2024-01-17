import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Prueba del control de Notebook")
        self.cuaderno1 = ttk.Notebook(self.ventana1)

        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Button")
        self.label1=ttk.Label(self.pagina1,text="La clase Button nos permite capturar el clic y lanzamiento")
        self.label1.grid(column=0,row=0)
        self.boton1=ttk.Button(self.pagina1,text="Ejemplo de boton")
        self.boton1.grid(column=0,row=1)
        self.boton2=ttk.Button(self.pagina1,text="Ejemplo de boton inactivo",state="disabled")
        self.boton2.grid(column=0, row=2)

        self.cuaderno1.grid(column=0,row=0)
        self.ventana1.mainloop()

aplicacion1=Aplicacion()
        