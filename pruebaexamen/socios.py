import mysql.connector

class Socios:
    def __init__(self):
        self.conexion=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bd_scott")

    
    def get_jefes(self):
        cursor=self.conexion.cursor()
        jefe="SELECT ENAME,EMPNO FROM EMP WHERE EMPNO IN(SELECT DISTINCT MGR FROM EMP WHERE MGR IS NOT NULL) ORDER BY 1"
        cursor.execute(jefe)
        vuelta=cursor.fetchall
        return vuelta
    
    def get_dept(self):
        cursor=self.conexion.cursor()
        dept="SELECT DNAME, DEPTNO from DEPT ORDER BY 1"
        cursor.execute(dept)
        vuelta=cursor.fetchall
        return vuelta