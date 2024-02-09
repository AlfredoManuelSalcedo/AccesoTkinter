import mysql.connector

class base:
    def verificar():
        try:
            connection = mysql.connector.connect(host='localhost', database='sys', user='root', password='root')
            if connection.is_connected():
                cursor = connection.cursor()

                cursor.execute("CREATE DATABASE CAJEROS")
                print("Base de datos creada")

        except mysql.connector.Error as e:
            print("La base de datos ya existe")
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


 