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
        self.precio=float(self.compra.get())
        self.compra=self.pago.get("1.0","end-1c")
        tb = self.compra.split("#")
        separador = []
        cantidad_total = 0.00
        for i in tb:
            separador = i.split("-")
            cantidad_total += float(separador[1]) * int(separador[0])
        resta_cantidad = cantidad_total - self.precio
        resta_cantidad = round(resta_cantidad, 2)
        print("resto", resta_cantidad)
        if self.precio <= cantidad_total:
             try:
                conn = mysql.connector.connect(host="localhost",port=3306,user="root",password="root",database="CAJEROS")
                cursor = conn.cursor()
                cambio = False
                for i in tb:
                    separador = i.split("-")
                    SQL_UPDATE = f"UPDATE CAJERO SET CANTIDAD = CANTIDAD + {separador[0]} WHERE MONEDA = {separador[1]}"
                    cursor.execute(SQL_UPDATE)
                    conn.commit()
                while resta_cantidad > 0.01:
                    cursor.execute("SELECT * FROM CAJERO WHERE CANTIDAD > 0 ORDER BY MONEDA DESC")
                    results = cursor.fetchall()
                    for row in results:
                        bbdd_moneda = row[0]
                        bbdd_cantidad = row[1]
                        self.vueltas.insert(bbdd_moneda,bbdd_cantidad)
                        print("moneda", bbdd_moneda)
                        print("cantidad", bbdd_cantidad)
                        if bbdd_moneda <= resta_cantidad:
                            resto = float(resta_cantidad) / float(bbdd_moneda)
                            resto = float(resto)
                            print("resto", resto)
                            if resto <= bbdd_cantidad:
                                resta_cantidad -= float(bbdd_moneda) * resto
                                SQL_UPDATE2 = f"UPDATE CAJERO SET CANTIDAD = CANTIDAD - {resto} WHERE MONEDA = {bbdd_moneda}"
                                cursor.execute(SQL_UPDATE2)
                                conn.commit()
                                cambio = True
                            else:
                                resta_cantidad -= bbdd_moneda * bbdd_cantidad
                                SQL_UPDATE2 = f"UPDATE CAJERO SET CANTIDAD = CANTIDAD - {bbdd_cantidad} WHERE MONEDA = {bbdd_moneda}"
                                cursor.execute(SQL_UPDATE2)
                                conn.commit()
                                cambio = True
                    if not cambio:
                        break
             except mysql.connector.Error as e:
                print(e)
             finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()
        else:
            print(f"Debe ingresar {resta_cantidad} a la compra")
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


class spinbox(Spinbox):
    def __init__(self, ventana, fila, columna, vari):
        self.contenido=ventana
        cadena =('w'+str(vari)).replace('.','')
        zz=ttk.Spinbox(ventana,name=cadena,from_=0,to=globals()[cadena].get(),increment=1,justify="right",textvariable=globals()[cadena])
        zz.configure(font="Arial 12",width=8)
        zz.grid(padx=5,pady=5,row=fila,column=columna)
      
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
    