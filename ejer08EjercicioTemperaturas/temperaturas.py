import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb 
from tkinter import PhotoImage
import calculos

class temperaturastabla:
    def __init__(self):
        self.calculos=calculos.calculo()
        self.ventana1=tk.Tk()
        self.ventana1.title("Temperatura")

        self.ventana1.resizable(False,False)
        self.ventana1.configure(background="#70A3CC")
        w = 525
        h = 400
        x=(self.ventana1.winfo_screenwidth() / 2) - (w/2)
        y = (self.ventana1.winfo_screenheight()/2)-(h/2)
        self.ventana1.geometry('%dx%d+%d+%d' % (w, h, x, y))
        
        self.Insertar()
        self.ventana1.mainloop()
    
   
    def Insertar(self):
        self.labelframe1=ttk.LabelFrame(self.ventana1, text="Temperaturas")
        self.labelframe1.grid(column=0,row=0,padx=125,pady=10)
 #==============================CELSIUS===========================#
        self.label1=ttk.Label(self.labelframe1, text="Celsius:").grid(column=0,row=0,padx=4,pady=4)
        
        self.celsius=tk.DoubleVar()
        self.entryc=ttk.Entry(self.labelframe1,textvariable=self.celsius, width=10)
        self.entryc.grid(column=1,row=0,padx=4,pady=4)
        

        self.boton=ttk.Button(self.labelframe1, text="+1", width="5", command=self.sumarc)
        self.boton.grid(column=2,row=0,padx=4,pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="-1", width="5", command=self.restarc)
        self.boton1.grid(column=3,row=0,padx=4,pady=4)
#==============================KELVIN===========================#
        self.label2=ttk.Label(self.labelframe1, text="Kelvin:")
        self.label2.grid(column=0,row=1,padx=4,pady=4)
    
        self.kelvin=tk.DoubleVar()
        self.entryk=ttk.Entry(self.labelframe1,textvariable=self.kelvin, width=10)
        self.entryk.grid(column=1,row=1,padx=4,pady=4)
        

        self.boton2=ttk.Button(self.labelframe1, text="+1", width="5", command=self.sumark)
        self.boton2.grid(column=2,row=1,padx=4,pady=4)
        self.boton3=ttk.Button(self.labelframe1, text="-1", width="5", command=self.restark)
        self.boton3.grid(column=3,row=1,padx=4,pady=4)
#==============================FARENHEIT===========================#
        self.label3=ttk.Label(self.labelframe1, text="Fahrenheit:")
        self.label3.grid(column=0,row=2,padx=4,pady=4)
    
        self.farenheit=tk.DoubleVar()
        self.entryf=ttk.Entry(self.labelframe1,textvariable=self.farenheit, width=10)
        self.entryf.grid(column=1,row=2,padx=4,pady=4)
        

        self.boton4=ttk.Button(self.labelframe1, text="+1", width="5", command=self.sumarf)
        self.boton4.grid(column=2,row=2,padx=4,pady=4)
        self.boton5=ttk.Button(self.labelframe1, text="-1", width="5", command=self.restarf)
        self.boton5.grid(column=3,row=2,padx=4,pady=4)

        self.celsius.trace_add("write",self.actualizarc())
        self.kelvin.trace_add("write",self.actualizark())
        self.farenheit.trace_add("write",self.actualizarf())
        
    def sumarc(self):
        self.celsius.set(self.celsius.get()+1)
        self.actualizarc()
    def restarc(self):
        self.celsius.set(self.celsius.get()-1)
        self.actualizarc()
    def sumark(self):
        self.kelvin.set(self.kelvin.get()+1)
    def restark(self):
        self.kelvin.set(self.kelvin.get()-1)
    def sumarf(self):
        self.farenheit.set(self.farenheit.get()+1)
    def restarf(self):
        self.farenheit.set(self.farenheit.get()-1)

    def actualizarc(self):
        self.kelvin.set(self.celsius.get()+ 273.15)
        self.farenheit.set(((self.celsius.get()*9)/5)+32)
    def actualizark(self):
        self.celsius.set(self.kelvin.get()-273.15)
        self.farenheit.set((((self.kelvin.get()-273.15)*9)/5)+32)
    def actualizarf(self):
        self.celsius.set(((self.farenheit.get()-32)*5)/9)
        self.kelvin.set((((self.farenheit.get()-32)*5)/9)+273.15)


        

aplicacion=temperaturastabla()