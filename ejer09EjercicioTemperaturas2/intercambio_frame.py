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

        self.cambio_frame()

    def cambio_frame(self):
        frame =self.frames[self.valor.get()]
        frame.reset()
        frame.tkraise()

class CrearFrame(ttk.Frame):
    def __init__(self,aplicacion,nombre,funcion):
        super().__init__(aplicacion)
        self.nombre = nombre
        self.funcion = funcion

        opciones = {'padx':5,'pady':5}

        ttk.Label(self,text=self.nombre).grid(column=0,row=0,sticky='w',**opciones)

        self.temperatura = tk.StringVar()
        self.temperatura_entry = tk.Entry(self, textvariable=self.temperatura)
        self.temperatura_entry.grid(column=1,row=0,sticky='w',**opciones)

        tk.Button(self,text="Convertir",command=self.conversion).grid(column=2,row=0,sticky='w',**opciones)
        self.VResultado = ttk.Label(self)
        self.VResultado.grid(columnspan=3,row=1,**opciones)
        
        self.grid(column=0,row=0,padx=5,pady=5,sticky='nsew')
        self.temperatura_entry.focus()

    def conversion(self,event=None):
        try:
            resultado=self.funcion(float(self.temperatura.get()))
            self.VResultado.config(text=resultado)
        except ValueError as error:
            mb.showerror(title='ERROR', message=error)

    def reset(self):
        self.temperatura_entry.delete(0,'end')
        self.VResultado.text= ''
        


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