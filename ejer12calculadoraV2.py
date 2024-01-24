from tkinter import *
from tkinter import messagebox

class Calculadora(Frame):
    def __init__(self,ventana):
        super().__init__(ventana)
        self.grid()
        self.botones()
        ap.mainloop()
    
    def botones(self):
        estilo = {"font":("Arial",16),"bg":"white","fg":'red',"highlightbackground":'red'}
        estilo1 = {"font":("Arial",14),"bg":"white","fg":'black',"highlightbackground":'white'}

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

    def remplazarTexto(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)


    def añadir(self,text):
        actualText = self.display.get()
        textLength = len(actualText)
        if actualText == "0":
            self.remplazarTexto(text)
        else:
            self.display.insert(textLength, text)
    
    def evaluar(self):
        try:
            self.remplazarTexto(eval(self.display.get()))
        except (SyntaxError, AttributeError):
            messagebox.showerror("Error", "SyntaxError")
            self.remplazarTexto("0")
        except ZeroDivisionError:
            messagebox.showerror("Error","No se puede divir entre 0")
            self.remplazarTexto("0")

    def contineSigno(self):
        lista= ["*","/","+","-"]
        display = self.display.get()
        for c in display:
            if c in lista:
                return True
        return False

    def cambioSigno(self):
        if self.contineSigno():
            self.evaluar()
        firstChar = self.display.get()[0]
        if firstChar == "0":
            pass
        elif firstChar =="-":
            self.display.delete(0)
        else:
            self.display.insert(0,"-")
    
    def inversa(self):
        self.display.insert(0,"1/(")
        self.añadir(")")
        self.evaluar()

    def borrarUltimoCaracter(self):
        textLength= len(self.display.get())
        if textLength >=1:
            self.display.delete(textLength-1 , END)
        elif textLength ==1:
            self.remplazarTexto("0")






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
    