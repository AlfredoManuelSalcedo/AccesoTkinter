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

# Función para insertar datos en la tabla 'emp'
def insertar_datos():
    try:
        empno = int(entry_empno.get())
        ename = entry_ename.get()
        job = entry_job.get()
        mgr = int(combo_mgr.get())
        hiredate = entry_hiredate.get()
        sal = float(entry_sal.get())
        comm = float(entry_comm.get())
        deptno = combo_dept.get()

        # Obtener el DEPTNO correspondiente al DNAME seleccionado
        cursor.execute("SELECT DEPTNO FROM dept WHERE DNAME = %s", (deptno,))
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

# Crear pestañas
pestañas = ttk.Notebook(ventana)

# Pestaña 1: Formulario de Inserción
pestana1 = ttk.Frame(pestañas)
pestañas.add(pestana1, text="Inserción de Datos")

# Labels y Entry para el formulario
label_empno = tk.Label(pestana1, text="EMPNO:")
entry_empno = tk.Entry(pestana1)

label_ename = tk.Label(pestana1, text="ENAME:")
entry_ename = tk.Entry(pestana1)

label_job = tk.Label(pestana1, text="JOB:")
entry_job = tk.Entry(pestana1)

label_mgr = tk.Label(pestana1, text="MGR:")
cursor.execute("SELECT ENAME,EMPNO FROM EMP WHERE EMPNO IN(SELECT DISTINCT MGR FROM EMP WHERE MGR IS NOT NULL) ORDER BY 1")
mgr_options = [row[0] for row in cursor.fetchall()]
combo_mgr = ttk.Combobox(pestana1, values=mgr_options)

label_hiredate = tk.Label(pestana1, text="HIREDATE:")
entry_hiredate = tk.Entry(pestana1)

label_sal = tk.Label(pestana1, text="SAL:")
entry_sal = tk.Entry(pestana1)

label_comm = tk.Label(pestana1, text="COMM:")
entry_comm = tk.Entry(pestana1)

label_dept = tk.Label(pestana1, text="DEPTNO:")
cursor.execute("SELECT DNAME, DEPTNO from DEPT ORDER BY 1")
dept_options = [row[0] for row in cursor.fetchall()]
combo_dept = ttk.Combobox(pestana1, values=dept_options)

# Botón para realizar la inserción
btn_insertar = tk.Button(pestana1, text="Insertar Datos", command=insertar_datos)

# Posicionar elementos en la pestaña 1
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

# Pestaña 2: Visualización de Datos (puedes agregar más funcionalidades aquí)

# Mostrar pestañas
pestañas.pack(expand=1, fill="both")

# Ejecutar la aplicación
ventana.mainloop()

# Cerrar la conexión a la base de datos al salir de la aplicación
conexion.close()
 