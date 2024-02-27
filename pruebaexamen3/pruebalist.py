import tkinter as tk
from tkinter import ttk
import mysql.connector


class crearLabel(tk.Label):
    def __init__(self, tk, Frame, array, contador):
        super().__init__()
        contadorc = 1
        for t in array:
            ttk.Label(Frame, text=t, width=20).grid(row=contador, column=contadorc, padx=10, pady=10)
            contadorc += 1
class ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.cuaderno = ttk.Notebook(self)
        self.cuaderno.grid(column=0, row=0, padx=10, pady=10)
        self.Frame = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.Frame, text='s')
        self.labelframe1 = ttk.LabelFrame(self.Frame, text="EMP")
        self.labelframe1.grid(column=0, row=0, padx=10, pady=10)
        self.crearDisplay()

    def crearDisplay(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="bd_scott"
            )
            cursor = conn.cursor()
            cursor.execute("select * from emp")
            resultados = cursor.fetchall()
            self.contador=1
            for r in resultados:
                if self.contador==20:
                    break
                self.contador = self.contador+1
                EMPNO = r[0]
                ENAME = r[1]
                JOB = r[2]
                MGR = r[3]
                SAL = r[4]
                COMM = r[5]
                DEPTNO = r[6]
                HIREDATE = r[7]
                array = [EMPNO, ENAME, JOB, MGR, SAL, COMM, DEPTNO, HIREDATE]
                print(array)
                crearLabel(self, self.Frame, array, self.contador)
            cursor.close()
            conn.close()
        except mysql.connector.Error as e:
            print(f"SQL State: {e.sqlstate}\n{e.msg}")



if __name__ == '__main__':
    ap = ventana()
    ap.mainloop()