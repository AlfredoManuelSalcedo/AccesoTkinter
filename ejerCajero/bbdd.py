import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import cajero
class base:
    def verificar():
        try:
            connection = mysql.connector.connect(host='localhost', database='sys', user='root', password='root')
            if connection.is_connected():
                cursor = connection.cursor()

                cursor.execute("CREATE DATABASE CAJEROS")
                print("Base de datos creada")

        except mysql.connector.Error as e:
            print("BBDD conectada")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("Connection close")
    
    def verificartbl():
        SQL_CREATE = "CREATE TABLE CAJERO(MONEDA DECIMAL(10,2) PRIMARY KEY, CANTIDAD INT CHECK(CANTIDAD>=0))"
        SQL_INSERT = "INSERT INTO CAJERO VALUES (%s, %s)"
        numeros = [5, 2, 1]

        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="CAJEROS")
            cursor = conn.cursor()

            cursor.execute(SQL_CREATE)

            for i in range(-2, 3):
                for j in range(len(numeros)):
                    cursor.execute(SQL_INSERT, (10 ** i * numeros[j], 10))

            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            pass
        
   # def labels(vnt):
    #    ttk.Label(vnt, text="Monedas").grid(column=0, row=0, padx=10, pady=10)
    #    ttk.Label(vnt, text="Cantidad").grid(column=1, row=0, padx=10, pady=10)
    #    SQL_COUNT = "SELECT MONEDA FROM CAJERO"
    #    conn = mysql.connector.connect(host="localhost", user="root", password="root", database="CAJEROS")
     #   cursor = conn.cursor()
     #   cursor.execute(SQL_COUNT)
     #   records = cursor.fetchall()
     #   fila = 1
     #   for row in records:
     #       ttk.Label(vnt, text=row[0]).grid(column=0, row=fila, padx=10, pady=10)
     #       fila += 1

    #def recargar():
    #    try:
    #        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="CAJEROS")
    #        query="select * from cajero order by moneda desc"
    #        cursor = conn.cursor()
    #        cursor.execute(query)
    #        records = cursor.fetchall()
    #        for row in records:
    #            cadena =('w'+str(row[0])).replace('.','')
    #            globals()[cadena].set[row[1]]
    #    except mysql.connector.Error as error:
    #        print(error)
    #    finally:
    #        cursor.close()

    #def llenar():
    #    Label(cajero.marco1,1,0,"Moneda")
    #    Label(cajero.marco1,1,1,"Cantidad")
    #    k=2
    #    try:
    #        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="CAJEROS")
    #        query="select * from cajero order by moneda desc"
    #        cursor = conn.cursor()
    #        cursor.execute(query)
    #        records = cursor.fetchall()
    #        for row in records:
    #            cadena =('w'+str(row[0])).replace('.','')
    #            globals()[cadena] = DoubleVar(value=row[1])
    #            cajero.label(cajero.marco1,k,0,str(row[0]))
    #            cajero.spinbox(cajero.marco1,k,1,row[0])
    #            k=k+1
    #    except mysql.connector.Error as error:
    #        print(error)
    #    finally:
    #        cursor.close()

    
    
    #def selects(vnt):
        #SQL_SELECT="SELECT * FROM CAJERO"
        #conn = mysql.connector.connect(host="localhost", user="root", password="root", database="CAJEROS")
        #cursor = conn.cursor()
        #cursor.execute(SQL_SELECT)
        #records = cursor.fetchall()
        #fila = 1
        #for row in records:
            #Spinbox1=ttk.Spinbox(vnt, from_=0, to=2000, width=5)        
            #Spinbox1.set(row[1])
            #Spinbox1.grid(row=fila, column=1)
            #Spinbox1.bind("<Button>",lambda click, valor=row[0],sb=Spinbox1: base.cambio(click,v=valor,spb=sb))
            #fila += 1
    
    #def cambio(this,*args,v,spb):
        #print(spb.get())
        