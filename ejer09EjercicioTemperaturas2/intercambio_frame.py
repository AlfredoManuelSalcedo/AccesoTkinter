import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import convertir as cv

class ControlFrame(ttk.LabelFrame):
    def __init__(self, aplicacion):
        super().__init__(aplicacion)
        self['text']='Opciones'

        self.valor= tk.IntVar()

        ttk.Radiobutton(self, text='F a C', value=0,variable=self.valor, command=self.cambio_frame).grid(column=0, row=0,padx=5,pady=5)

        ttk.Radiobutton(self, text='C a F', value=1,variable=self.valor, command=self.cambio_frame).grid(column=1, row=0,padx=5,pady=5)

        ttk.Radiobutton(self, text='C a K', value=2,variable=self.valor, command=self.cambio_frame).grid(column=2, row=0,padx=5,pady=5)

        ttk.Radiobutton(self, text='K a C', value=3,variable=self.valor, command=self.cambio_frame).grid(column=3, row=0,padx=5,pady=5)

        ttk.Radiobutton(self, text='F a K', value=4,variable=self.valor, command=self.cambio_frame).grid(column=4, row=0,padx=5,pady=5)

        ttk.Radiobutton(self, text='K a F', value=5,variable=self.valor, command=self.cambio_frame).grid(column=5, row=0,padx=5,pady=5)

        self.grid(column=0,row=1,padx=5,pady=5,sticky='ew')

        self.frames = {}
        self.frames[0] = CrearFrame(aplicacion,"Fahrenheit",cv.Convertir.f_a_c)
        self.frames[1] = CrearFrame(aplicacion,"Celsius",cv.Convertir.c_a_k)
        self.frames[2] = CrearFrame(aplicacion,"Celsius",cv.Convertir.c_a_f)
        self.frames[3] = CrearFrame(aplicacion,"Kelvin",cv.Convertir.k_a_c)
        self.frames[4] = CrearFrame(aplicacion,"Fahrenheit",cv.Convertir.f_a_k)
        self.frames[5] = CrearFrame(aplicacion,"Kelvin",cv.Convertir.k_a_f)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Conversor Temperaturas")
        w=400
        h=200
        x = (self.winfo_screenwidth()/2)-(w/2)
        y = (self.winfo_screenheight()/2)-(h/2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(False,False)

if __name__ == "__main__":
    ap=App()
    ControlFrame(ap)
    ap.mainloop()