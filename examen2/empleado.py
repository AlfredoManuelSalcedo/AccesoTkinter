import mysql.connector

class Empleado:
    def __init__(self):
        self.conexion=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bd_scott")

    def nuevo_empleado(self, datos):
        cursor=self.conexion.cursor()
        sql="insert into emp(EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, datos)
        self.conexion.commit()

    def empleados(self):
        cursor=self.conexion.cursor()
        sql="SELECT EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO from emp"
        cursor.execute(sql)
        vuelta=cursor.fetchall()
        return vuelta
    
    def borrar_empleado(self, datos):
        cursor=self.conexion.cursor()
        sql="DELETE FROM emp WHERE EMPNO=%s"
        cursor.execute(sql,datos)
        n=cursor.rowcount
        self.conexion.commit()
        return n #devolver las filas borradas
    
    def consultaEmpleado(self, datos):
        cursor=self.conexion.cursor()
        sql="SELECT EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO FROM emp where EMPNO=%s"
        cursor.execute(sql,datos)
        vuelta=cursor.fetchall()
        return vuelta