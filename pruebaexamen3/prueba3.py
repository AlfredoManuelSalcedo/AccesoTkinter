import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="bd_scott"
)
cursor = conexion.cursor()

# Obtener la lista de ENAME de la tabla 'emp'
cursor.execute("SELECT ENAME FROM emp")
ename_options = [row[0] for row in cursor.fetchall()]

# Función para insertar datos en la tabla 'emp'
def insertar_datos():
    try:
        empno = int(entry_empno.get())
        ename = entry_ename.get()
        job = entry_job.get()
        mgr_ename = combo_mgr.get()
        hiredate = entry_hiredate.get()
        sal = float(entry_sal.get())
        comm = float(entry_comm.get())
        dept_dname = combo_dept.get()

        # Obtener el EMPNO correspondiente al ENAME seleccionado
        cursor.execute("SELECT EMPNO FROM emp WHERE ENAME = %s", (mgr_ename,))
        result = cursor.fetchone()
        if result:
            mgr = result[0]
        else:
            messagebox.showerror("Error", "Empleado (MGR) no encontrado")
            return

        # Obtener el DEPTNO correspondiente al DNAME seleccionado
        cursor.execute("SELECT DEPTNO FROM dept WHERE DNAME = %s", (dept_dname,))
        result = cursor.fetchone()
        if result:
            deptno = result[0]
        else:
            messagebox.showerror("Error", "Departamento no encontrado")
            return

        # Insertar datos en la tabla 'emp'
        cursor.execute("INSERT INTO emp (EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO) "
                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                       (empno, ename, job, mgr, hiredate, sal, comm, deptno))
        conexion.commit()

        messagebox.showinfo("Éxito", "Datos insertados correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"Error al insertar datos: {str(e)}")


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Inserción de Datos")

# Labels y Entry para el formulario
label_empno = tk.Label(ventana, text="EMPNO:")
entry_empno = tk.Entry(ventana)
label_ename = tk.Label(ventana, text="ENAME:")
entry_ename = tk.Entry(ventana)
label_job = tk.Label(ventana, text="JOB:")
entry_job = tk.Entry(ventana)
label_mgr = tk.Label(ventana, text="MGR:")
combo_mgr = ttk.Combobox(ventana, values=ename_options)
label_hiredate = tk.Label(ventana, text="HIREDATE:")
entry_hiredate = tk.Entry(ventana)
label_sal = tk.Label(ventana, text="SAL:")
entry_sal = tk.Entry(ventana)
label_comm = tk.Label(ventana, text="COMM:")
entry_comm = tk.Entry(ventana)
label_dept = tk.Label(ventana, text="DEPTNO:")
cursor.execute("SELECT DNAME FROM dept")
dept_options = [row[0] for row in cursor.fetchall()]
combo_dept = ttk.Combobox(ventana, values=dept_options)

# Botón para realizar la inserción
btn_insertar = tk.Button(ventana, text="Insertar Datos", command=insertar_datos)

# Posicionar elementos en la ventana
label_empno.grid(row=0, column=0, padx=5, pady=5)
entry_empno.grid(row=0, column=1, padx=5, pady=5)
label_ename.grid(row=1, column=0, padx=5, pady=5)
entry_ename.grid(row=1, column=1, padx=5, pady=5)
label_job.grid(row=2, column=0, padx=5, pady=5)
entry_job.grid(row=2, column=1, padx=5, pady=5)
label_mgr.grid(row=3, column=0, padx=5, pady=5)
combo_mgr.grid(row=3, column=1, padx=5, pady=5)
label_hiredate.grid(row=4, column=0, padx=5, pady=5)
entry_hiredate.grid(row=4, column=1, padx=5, pady=5)
label_sal.grid(row=5, column=0, padx=5, pady=5)
entry_sal.grid(row=5, column=1, padx=5, pady=5)
label_comm.grid(row=6, column=0, padx=5, pady=5)
entry_comm.grid(row=6, column=1, padx=5, pady=5)
label_dept.grid(row=7, column=0, padx=5, pady=5)
combo_dept.grid(row=7, column=1, padx=5, pady=5)
btn_insertar.grid(row=8, column=0, columnspan=2, pady=10)

# Ejecutar la aplicación
ventana.mainloop()

# Cerrar la conexión a la base de datos al salir de la aplicación
conexion.close()