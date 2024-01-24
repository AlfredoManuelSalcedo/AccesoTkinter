from tkinter import *
from tkinter import messagebox

class Calculadora(Frame):
    def __init__(self,ventana):
        super().__init__(ventana)
        self.grid()
        self.botones()
    
    def botones(self):
        estilo = {"font":("Arial",16),"bg":"white","fg":'red',"highligthbackground":'red'}
        estilo1 = {"font":("Arial",14),"bg":"white","fg":'black',"highligthbackground":'white'}

        self.display=Entry(self, font=("Arial",24),relief=RIDGE,justify=RIGHT,bg='darkblue',fg='red',borderwidth=0)
        self.display.insert(0,"0")
        self.display.grid(row=0,column=0,columnspan=4,sticky="nsew")

        Button(self, text="CE",**estilo, command=lambda: self.remplazarTexto("0")).grid(row=1,column=0,sticky="nsew")
        Button(self, text="1/x",**estilo, command=lambda: self.inversa()).grid(row=1,column=2,sticky="nsew")
        Button(self, text="Del",**estilo, command=lambda: self.borrarUltimoCaracter()).grid(row=1,column=1,sticky="nsew")
        Button(self, text="0",**estilo1, command=lambda: self.añadir("0")).grid(row=5,column=1,sticky="nsew")
        Button(self, text="1",**estilo1, command=lambda: self.añadir("1")).grid(row=4,column=0,sticky="nsew")
        Button(self, text="2",**estilo1, command=lambda: self.añadir("2")).grid(row=4,column=1,sticky="nsew")
        Button(self, text="3",**estilo1, command=lambda: self.añadir("3")).grid(row=4,column=2,sticky="nsew")
        Button(self, text="4",**estilo1, command=lambda: self.añadir("4")).grid(row=3,column=0,sticky="nsew")
        Button(self, text="5",**estilo1, command=lambda: self.añadir("5")).grid(row=3,column=1,sticky="nsew")
        Button(self, text="6",**estilo1, command=lambda: self.añadir("6")).grid(row=3,column=2,sticky="nsew")
        Button(self, text="7",**estilo1, command=lambda: self.añadir("7")).grid(row=2,column=0,sticky="nsew")
        Button(self, text="8",**estilo1, command=lambda: self.añadir("8")).grid(row=2,column=1,sticky="nsew")
        Button(self, text="9",**estilo1, command=lambda: self.añadir("9")).grid(row=2,column=2,sticky="nsew")
        Button(self, text="/",**estilo, command=lambda: self.añadir("/")).grid(row=1,column=3,sticky="nsew")
        Button(self, text="*",**estilo, command=lambda: self.añadir("*")).grid(row=2,column=3,sticky="nsew")
        Button(self, text="-",**estilo, command=lambda: self.añadir("-")).grid(row=3,column=3,sticky="nsew")
        Button(self, text="+",**estilo, command=lambda: self.añadir("+")).grid(row=4,column=3,sticky="nsew")
        Button(self, text="+/-",**estilo, command=lambda: self.cambioSigno()).grid(row=5,column=0,sticky="nsew")
        Button(self, text=".",**estilo, command=lambda: self.añadir(".")).grid(row=5,column=2,sticky="nsew")
        Button(self, text="=",**estilo, command=lambda: self.evaluar()).grid(row=5,column=3,sticky="nsew")







class App(Tk):
    def __init__(self):
        super().__init__()
        self.configure(padx=30,pady=30)
        self.title("Calculadora")
        w=425
        h=300
        x = (self.winfo_screenwidth()/2)-(w/2)
        y = (self.winfo_screenheight()/2)-(h/2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(False,False)

if __name__ == "__main__":
    ap=App()
    Calculadora(ap)
    