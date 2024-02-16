import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import bbdd

class Aplicacion(Tk):
    def __init__(self):
        super().__init__()
        self.iniciar()
        bbdd.base.verificar()
        bbdd.base.verificartbl()
        self.color="#4bdddb"
        self.marco1=frame(self,180,self.color,(40,40))
        self.marco2=frame(self,420,self.color,(0,40))
        self.llenar()
        self.recargar()
        self.compra=273

        label2(self.marco2,"Comprar:")
        
    
    def recargar(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="CAJEROS")
            query="select * from cajero order by moneda desc"
            cursor = conn.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            for row in records:
                cadena =('w'+str(row[0])).replace('.','')
                globals()[cadena].set(row[1])
        except mysql.connector.Error as error:
            print(error)
        finally:
            cursor.close()

    def llenar(self):
        label(self.marco1,1,0,"Moneda")
        label(self.marco1,1,1,"Cantidad")
        k=2
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="CAJEROS")
            query="select * from cajero order by moneda desc"
            cursor = conn.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            for row in records:
                cadena =('w'+str(row[0])).replace('.','')
                globals()[cadena] = DoubleVar(value=row[1])
                label(self.marco1,k,0,str(row[0]))
                spinbox(self.marco1,k,1,row[0])
                k=k+1
        except mysql.connector.Error as error:
            print(error)
        finally:
            cursor.close()

        

    def iniciar(self):
        self.configure(padx=30,pady=30)
        self.title("Cajero")
        w=425
        h=700
        x = (self.winfo_screenwidth()/2)-(w/2)
        y = (self.winfo_screenheight()/2)-(h/2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(False,False)
        self.configure(background="#4bdddb")


class spinbox(Spinbox):
    def __init__(self, ventana, fila, columna, vari):
        self.contenido=ventana
        cadena =('w'+str(vari)).replace('.','')
        zz=ttk.Spinbox(ventana,name=cadena,from_=0,to=globals()[cadena].get(),increment=1,justify="right",textvariable=globals()[cadena])
        zz.configure(font="Arial 12",width=9)
        zz.grid(padx=5,pady=5,row=fila,column=columna)
      
class label(Label):
    def __init__(self, ventana, fila, columna, texto):
        self.contenido=ventana
        label1=ttk.Label(ventana,text=texto)
        label1.configure(font="Arial 12 bold", width=10)
        label1.grid(padx=5,pady=5,row=fila,column=columna)

class label2(Label):
    def __init__(self, ventana, fila, columna, texto):
        self.contenido=ventana
        label1=ttk.Label(ventana,text=texto)
        label1.configure(font="Arial 12 bold", width=10)
        label1.grid(padx=5,pady=5,row=fila,column=columna)
 
class frame(Frame):
    def __init__(self,ventana,ancho,color,vpadx):
        super().__init__(bg=color,height=730,width=ancho,pady=40)
        self.conti=ventana
        ipadding={'ipadx':10,'ipady':10}
        self.pack(**ipadding,side='left',padx=vpadx)
        self.pack_propagate(False)
    

if __name__ == "__main__":
    ap=Aplicacion()
    ap.mainloop()
    