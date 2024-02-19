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
        self.compra=DoubleVar().set(273)

        label2(self.marco2,"Comprar:")
        self.compra=Spinbox(self.marco2,name="compra",from_=0,to=10000,increment=1,justify="right",textvariable=self.compra)
        self.compra.config(font="Arial 12",width=25)
        self.compra.pack(fill=Y)
        self.compra.pack_propagate(False)
        
        Frame(self.marco2,bg=self.color,height=60,bd=0,pady=10).pack(fill=X)

        label2(self.marco2,"Pago:")
        self.pago=Text(self.marco2,height=5)
        self.pago.pack()
        self.pago.pack_propagate(False)
        scrollbar= Scrollbar(self.pago)
        scrollbar.pack(side=RIGHT,fill=Y)
        self.pago.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.pago.yview)

        Frame(self.marco2,bg=self.color,height=60,bd=0,pady=10).pack(fill=X)

        label2(self.marco2,"Vueltas:")
        self.vueltas=Text(self.marco2,height=12)
        self.vueltas.pack()
        self.vueltas.pack_propagate(False)
        scrollbar2= Scrollbar(self.vueltas)
        scrollbar2.pack(side=RIGHT,fill=Y)
        self.vueltas.config(yscrollcommand=scrollbar2.set)
        scrollbar2.config(command=self.vueltas.yview)

        Frame(self.marco2,bg=self.color,height=40,bd=0,pady=10).pack(fill=X)
        self.boton = Button(self.marco2, text="Comprar",command=self.calcular)
        self.boton.pack()
        self.boton.pack_propagate(False)

    def calcular(self):
        self.costo=float(self.compra.get())
        self.dinero=self.pago.get("1.0","end-1c")
        tb = self.dinero.split('#')
        cantidad_total = 0.0
        for i in tb:
            matriz2 = i.split('-')
            cantidad_total += int(matriz2[0]) * float(matriz2[1])
        resto_cantidad = cantidad_total - self.costo
        resto_cantidad = round(resto_cantidad, 2)
        self.vueltas_text=""
        if self.costo <= cantidad_total:
         try:
            sentencia = f"SELECT * from cajero where CANTIDAD > 0 order by MONEDA DESC"
            connection = mysql.connector.connect(host='localhost', database='CAJEROS', user='root', password='root')
            cursor = connection.cursor()
            for i in tb:
                matriz2 = i.split('-')
                sentencia2 = f"UPDATE cajero set CANTIDAD = CANTIDAD + {matriz2[0]} where MONEDA = {matriz2[1]}"
                cursor.execute(sentencia2)
                connection.commit()
            while resto_cantidad > 0.01:
                cursor.execute(sentencia)
                records = cursor.fetchall()
                for row in records:
                    bbdd_cantidad = int(row[1])
                    bbdd_moneda = float(row[0])

                    if bbdd_moneda <= resto_cantidad:
                        resto = int(resto_cantidad / bbdd_moneda)

                        if resto <= bbdd_cantidad:
                            resto_cantidad = round(resto_cantidad - (bbdd_moneda * resto), 2)
                            sentencia3 = f"UPDATE cajero set CANTIDAD = CANTIDAD - {resto} where MONEDA = {bbdd_moneda}"
                            cursor.execute(sentencia3)
                            connection.commit()
                            self.vueltas_text += f"{resto} de {bbdd_moneda}€\n"
                        else:
                            resto_cantidad = round(resto_cantidad - (bbdd_moneda * bbdd_cantidad), 2)
                            sentencia3 = f"UPDATE cajero set CANTIDAD = CANTIDAD - {bbdd_cantidad} where MONEDA = {bbdd_moneda}"
                            cursor.execute(sentencia3)
                            connection.commit()
                            self.vueltas_text += f"{bbdd_cantidad} de {bbdd_moneda}€\n"
                self.vueltas.delete(1.0, END)
                self.vueltas.insert(INSERT, self.vueltas_text)
         except mysql.connector.Error as e:
            print(e)

         finally:
            if connection.is_connected():
                connection.close()
                cursor.close()
        else:
         print(f"Debe ingresar {resto_cantidad} para completar la compra")
        self.llenar()
        self.recargar()

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
        w=600
        h=700
        x = (self.winfo_screenwidth()/2)-(w/2)
        y = (self.winfo_screenheight()/2)-(h/2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(False,False)
        self.configure(background="#4bdddb")
    
    def cambio(this,*args,spb,v):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="CAJEROS")
            print(spb.get())
            print(v)
            sentencia="update cajero set cantidad="+str(spb.get())+" where moneda="+str(v)
            cursor = conn.cursor()
            cursor.execute(sentencia)
            conn.commit()
        except mysql.connector.Error as error:
            print(error)
        finally:
            cursor.close()


class spinbox(Spinbox):
    def __init__(self, ventana, fila, columna, vari):
        self.contenido=ventana
        cadena =('w'+str(vari)).replace('.','')
        zz=ttk.Spinbox(ventana,name=cadena,from_=0,to=100,increment=1,justify="right",textvariable=globals()[cadena])
        zz.configure(font="Arial 12",width=8)
        zz.grid(padx=5,pady=5,row=fila,column=columna)
        zz.bind("<Button>", lambda click,valor=vari,sb=zz: Aplicacion.cambio(click,spb=sb,v=valor))
      
class label(Label):
    def __init__(self, ventana, fila, columna, texto):
        self.contenido=ventana
        label1=ttk.Label(ventana,text=texto)
        label1.configure(font="Arial 12 bold", background="#4bdddb")
        label1.grid(padx=5,pady=5,row=fila,column=columna)

class label2(Label):
    def __init__(self, ventana, texto):
        self.contenido=ventana
        label1=ttk.Label(ventana,text=texto)
        label1.configure(font="Arial 12 bold", width=10)
        label1.pack(fill=X)
 
class frame(Frame):
    def __init__(self,ventana,ancho,color,pos):
        super().__init__(bg=color,height=730,width=ancho,pady=40)
        self.conti=ventana
        ipadding={'ipadx':10,'ipady':10}
        self.pack(**ipadding,side='left',padx=pos)
        self.pack_propagate(False)
    

if __name__ == "__main__":
    ap=Aplicacion()
    ap.mainloop()
    