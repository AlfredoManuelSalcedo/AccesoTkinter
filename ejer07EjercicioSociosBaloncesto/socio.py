import mysql.connector

class Socio:
    def __init__(self):
        self.conexion=mysql.connector.connect(host="localhost", user="root", passwd="root", database="baloncesto")
    
    def nuevo_socio(self, datos):
        cursor=self.conexion.cursor()
        sql="insert into socio(socioID, nombre, estatura, edad, localidad) values (%s,%s,%s,%s,%s)"
        cursor.execute(sql, datos)
        self.conexion.commit()
    
    def consultaSocio(self, datos):
        cursor=self.conexion.cursor()
        sql="SELECT nombre,estatura,edad,localidad FROM socio where socioID=%s"
        cursor.execute(sql,datos)
        vuelta=cursor.fetchall()
        return vuelta
    
    def socios(self):
        cursor=self.conexion.cursor()
        sql="SELECT socioID,nombre,estatura,edad,localidad from socio"
        cursor.execute(sql)
        vuelta=cursor.fetchall()
        return vuelta
    
    def borrar_socio(self, datos):
        cursor=self.conexion.cursor()
        sql="DELETE FROM socio WHERE socioID=%s"
        cursor.execute(sql,datos)
        n=cursor.rowcount
        self.conexion.commit()
        return n #devolver las filas borradas
    
    def modificar(self, datos):
        cursor=self.conexion.cursor()
        sql="UPDATE socio set nombre=%s, estatura=%s, edad=%s, localidad=%s where socioID=%s"
        cursor.execute(sql,datos)
        n=cursor.rowcount
        self.conexion.commit()
        return n #devuelve las filas modificadas
