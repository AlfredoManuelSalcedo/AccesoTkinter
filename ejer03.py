import tkinter as tk
from tkinter import ttk

class Application(ttk.Frame):

 def __init__(self, main_window):
  super().__init__(main_window)
  main_window.title("Posicionar elementos en Tcl/Tk")
  main_window.columnconfigure(0, weight=1)
  main_window.rowconfigure(0, weight=1)
 
  self.entry = ttk.Entry(self)
  self.entry.grid(row=0, column=0)
 
  self.button = ttk.Button(self, text="Presione aquí")
  self.button.grid(row=0, column=1)

  self.label = ttk.Label(self, text="¡Hola, mundo!")
  self.label.grid(row=1, column=0)

  self.grid(sticky="nsew")

#main
principal= tk.Tk()
app = Application(principal)
app.mainloop()