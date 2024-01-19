import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb 
from tkinter import scrolledtext as st 
import calculos

class temperaturastabla:
    def __init__(self):
        self.calculos=calculos.calculo()
        self.ventana1=tk.Tk()
        self.ventana1.title("Temperatura")

        self.ventana1.resizable(False,False)
        self.ventana1.configure(background="#70A3CC")
        w=525
        h = 400
        x=(self.ventana1.winfo_screenwidth() / 2) - (w/2)
        y = (self.ventana1.winfo_screenheight()/2)-(h/2)
        self.ventana1.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.ventana1.mainloop()

aplicacion=temperaturastabla()