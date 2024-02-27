import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
from tkinter import messagebox as mb 
import empleado
import mysql.connector

class Principal:
    def __init__(self):
        self.empleado=empleado.Empleado()
        self.ventana1=tk.Tk()
        self.ventana1.title("Scott")

        #PARAMETROS DE LA VENTANA
        self.ventana1.resizable(False,False)
        self.ventana1.configure(background="#6A9F80")
        w=525
        h = 400
        x=(self.ventana1.winfo_screenwidth() / 2) - (w/2)
        y = (self.ventana1.winfo_screenheight()/2)-(h/2)
        self.ventana1.geometry('%dx%d+%d+%d' % (w, h, x, y))

        #CREACION DEL CUADERNO CON SUS FUNCIONES
        self.cuaderno1 = ttk.Notebook(self.ventana1)
        self.Insertar()
        self.listado_completo()
        self.borrado()
        self.modificar()
        self.cuaderno1.grid(column=0, row=0, padx=10,pady=10)
        self.ventana1.mainloop()


    
    def Insertar(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Insertar socio")
        conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="bd_scott"
        )
        cursor = conexion.cursor()
        cursor.execute("SELECT ENAME,EMPNO FROM EMP WHERE EMPNO IN(SELECT DISTINCT MGR FROM EMP WHERE MGR IS NOT NULL) ORDER BY 1")
        ename_options = [row[0] for row in cursor.fetchall()]

        #CREACION
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Socio")
        self.labelframe1.grid(column=0,row=0,padx=5,pady=10)

        label_empno = tk.Label(self.pagina1, text="EMPNO:")
        self.entry_empno = tk.Entry(self.pagina1)

        label_ename = tk.Label(self.pagina1, text="ENAME:")
        self.entry_ename = tk.Entry(self.pagina1)

        label_job = tk.Label(self.pagina1, text="JOB:")
        self.entry_job = tk.Entry(self.pagina1)

        label_mgr = tk.Label(self.pagina1, text="MGR:")
        self.combo_mgr = ttk.Combobox(self.pagina1, values=ename_options)

        label_hiredate = tk.Label(self.pagina1, text="HIREDATE:")
        self.entry_hiredate = tk.Entry(self.pagina1)

        label_sal = tk.Label(self.pagina1, text="SAL:")
        self.entry_sal = tk.Entry(self.pagina1)

        label_comm = tk.Label(self.pagina1, text="COMM:")
        self.entry_comm = tk.Entry(self.pagina1)

        label_dept = tk.Label(self.pagina1, text="DEPTNO:")
        cursor.execute("SELECT DNAME FROM dept")
        dept_options = [row[0] for row in cursor.fetchall()]
        self.combo_dept = ttk.Combobox(self.pagina1, values=dept_options)

        btn_insertar = tk.Button(self.pagina1, text="Insertar Datos", command=self.insertar_datos)

        #POSICIONAMIENTO
        label_empno.grid(row=0, column=0, padx=5, pady=5)
        self.entry_empno.grid(row=0, column=1, padx=5, pady=5)

        label_ename.grid(row=1, column=0, padx=5, pady=5)
        self.entry_ename.grid(row=1, column=1, padx=5, pady=5)

        label_job.grid(row=2, column=0, padx=5, pady=5)
        self.entry_job.grid(row=2, column=1, padx=5, pady=5)

        label_mgr.grid(row=3, column=0, padx=5, pady=5)
        self.combo_mgr.grid(row=3, column=1, padx=5, pady=5)

        label_hiredate.grid(row=4, column=0, padx=5, pady=5)
        self.entry_hiredate.grid(row=4, column=1, padx=5, pady=5)

        label_sal.grid(row=5, column=0, padx=5, pady=5)
        self.entry_sal.grid(row=5, column=1, padx=5, pady=5)

        label_comm.grid(row=6, column=0, padx=5, pady=5)
        self.entry_comm.grid(row=6, column=1, padx=5, pady=5)

        label_dept.grid(row=7, column=0, padx=5, pady=5)
        self.combo_dept.grid(row=7, column=1, padx=5, pady=5)

        btn_insertar.grid(row=8, column=0, columnspan=2, pady=10)
    
    def insertar_datos(self):
        mgr_ename = self.combo_mgr.get()
        dept_dname = self.combo_dept.get()
        conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="bd_scott"
        )
        cursor = conexion.cursor()
        cursor.execute("SELECT EMPNO FROM emp WHERE ENAME = %s", (mgr_ename,))
        result = cursor.fetchone()
        if result:
            mgr = result[0]
        else:
            mb.showerror("Error", "Empleado (MGR) no encontrado")
            return
        
        cursor.execute("SELECT DEPTNO FROM dept WHERE DNAME = %s", (dept_dname,))
        result = cursor.fetchone()
        if result:
            deptno = result[0]
        else:
            mb.showerror("Error", "Departamento no encontrado")
            return
        datos=(self.entry_empno.get(),
               self.entry_ename.get(),
               self.entry_job.get(),
               mgr,
               self.entry_hiredate.get(),
               self.entry_sal.get(),
               self.entry_comm.get(),
               deptno)
        self.empleado.nuevo_empleado(datos)
        mb.showinfo("Información", "Los datos fueron cargados")

    def listado_completo(self):
        self.pagina3=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")

        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Empleado")
        self.labelframe3.grid(column=0,row=0,padx=5,pady=10)
   
        self.boton3=ttk.Button(self.labelframe3, text="Listado completo", command=self.listar)
        self.boton3.grid(column=0,row=0,padx=4,pady=4)

        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0, row=1,padx=10,pady=10)
    
    def listar(self):
        respuesta=self.empleado.empleados()
        self.scrolledtext1.delete("1.0", tk.END)
        for fila in respuesta:
            mgr_number = fila[3]
            dept_number = fila[7]
            conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="bd_scott"
            )
            cursor = conexion.cursor()
            cursor.execute("SELECT ENAME FROM emp WHERE EMPNO = %s", (mgr_number,))
            result = cursor.fetchone()
            if result:
                mgr_nom = result[0]
            else:
                if fila[1]=="KING":
                    mgr_nom = ""
                else:       
                    mb.showerror("Error", fila[1]+"Empleado (MGR) no encontrado")
                    return

            cursor.execute("SELECT DNAME FROM dept WHERE DEPTNO = %s", (dept_number,))
            result = cursor.fetchone()
            if result:
                dept_nom = result[0]
            else:
                mb.showerror("Error", "Departamento no encontrado")
                return
            self.scrolledtext1.insert(tk.END, "EMPNO:"+str(fila[0])+
                                              "\nENAME:"+fila[1]+
                                              "\nJOB:"+str(fila[2])+
                                              "\nMGR:"+mgr_nom+
                                              "\nHIREDATE:"+str(fila[4])+
                                              "\nSAL:"+str(fila[5])+
                                              "\nCOMM:"+str(fila[6])+
                                              "\nDEPTNO:"+dept_nom+
                                              "\n\n")
            
    def borrado(self):
        self.pagina4=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Borrado de empleados")

        self.labelframe4=ttk.LabelFrame(self.pagina4, text="Borrar")
        self.labelframe4.grid(column=0,row=0,padx=5,pady=10)

        self.label11=ttk.Label(self.labelframe4, text="EMPNO:")
        self.label11.grid(column=0, row=0,padx=4,pady=4)

        self.codigoborra=tk.StringVar()
        self.entrycodigoborra=ttk.Entry(self.labelframe4,textvariable=self.codigoborra)
        self.entrycodigoborra.grid(column=1,row=0,padx=4,pady=4)

        self.boton4=ttk.Button(self.labelframe4, text="Borrar", command=self.borrar)
        self.boton4.grid(column=1,row=1,padx=4,pady=4)
    
    def borrar(self):
        datos=(self.codigoborra.get(),)
        cantidad=self.empleado.borrar_empleado(datos)
        if cantidad==1:
            mb.showinfo("Información", "Empleado eliminado")
            self.codigoborra.set("")
        else:
            mb.showerror("Información", "No existe un articulo con dicho codigo")

    def modificar(self):
        self.pagina5 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5, text="Modificar empleado")
    
        self.labelframe5=ttk.LabelFrame(self.pagina5, text="Modificar:")
        self.labelframe5.grid(column=0,row=0,padx=5,pady=10)

        conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="bd_scott"
        )
        cursor = conexion.cursor()
        cursor.execute("SELECT ENAME,EMPNO FROM EMP WHERE EMPNO IN(SELECT DISTINCT MGR FROM EMP WHERE MGR IS NOT NULL) ORDER BY 1")
        ename_options2 = [row[0] for row in cursor.fetchall()]

        #CREACION
        self.labelframe2=ttk.LabelFrame(self.pagina5, text="Empleado")
        self.labelframe2.grid(column=0,row=0,padx=5,pady=10)

        label_empno2 = tk.Label(self.pagina5, text="EMPNO:")
        self.entry_empno2=tk.Entry(self.pagina5)

        label_ename2 = tk.Label(self.pagina5, text="ENAME:")
        self.entry_ename2 = tk.Entry(self.pagina5)

        label_job2 = tk.Label(self.pagina5, text="JOB:")
        self.entry_job2 = tk.Entry(self.pagina5)

        label_mgr2 = tk.Label(self.pagina5, text="MGR:")
        self.combo_mgr2 = ttk.Combobox(self.pagina5, values=ename_options2)

        label_hiredate2 = tk.Label(self.pagina5, text="HIREDATE:")
        self.entry_hiredate2 = tk.Entry(self.pagina5)

        label_sal2 = tk.Label(self.pagina5, text="SAL:")
        self.entry_sal2 = tk.Entry(self.pagina5)

        label_comm2 = tk.Label(self.pagina5, text="COMM:")
        self.entry_comm2 = tk.Entry(self.pagina5)

        label_dept2 = tk.Label(self.pagina5, text="DEPTNO:")
        cursor.execute("SELECT DNAME FROM dept")
        dept_options2 = [row[0] for row in cursor.fetchall()]
        self.combo_dept2 = ttk.Combobox(self.pagina5, values=dept_options2)

        btn_modificar = tk.Button(self.pagina5, text="Actualizar Datos", command=self.modifico)

        #POSICIONAMIENTO
        label_empno2.grid(row=0, column=0, padx=5, pady=5)
        self.entry_empno2.grid(row=0, column=1, padx=5, pady=5)

        label_ename2.grid(row=1, column=0, padx=5, pady=5)
        self.entry_ename2.grid(row=1, column=1, padx=5, pady=5)

        label_job2.grid(row=2, column=0, padx=5, pady=5)
        self.entry_job2.grid(row=2, column=1, padx=5, pady=5)

        label_mgr2.grid(row=3, column=0, padx=5, pady=5)
        self.combo_mgr2.grid(row=3, column=1, padx=5, pady=5)

        label_hiredate2.grid(row=4, column=0, padx=5, pady=5)
        self.entry_hiredate2.grid(row=4, column=1, padx=5, pady=5)

        label_sal2.grid(row=5, column=0, padx=5, pady=5)
        self.entry_sal2.grid(row=5, column=1, padx=5, pady=5)

        label_comm2.grid(row=6, column=0, padx=5, pady=5)
        self.entry_comm2.grid(row=6, column=1, padx=5, pady=5)

        label_dept2.grid(row=7, column=0, padx=5, pady=5)
        self.combo_dept2.grid(row=7, column=1, padx=5, pady=5)

        btn_modificar.grid(row=8, column=0, columnspan=2, pady=10)

    def modifico(self):
        mgr_ename2 = self.combo_mgr2.get()
        dept_dname2 = self.combo_dept2.get()
        conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="bd_scott"
        )
        cursor = conexion.cursor()
        cursor.execute("SELECT EMPNO FROM emp WHERE ENAME = %s", (mgr_ename2,))
        result = cursor.fetchone()
        if result:
            mgr2 = result[0]
        else:
            mb.showerror("Error", "Empleado (MGR) no encontrado")
            return
        
        cursor.execute("SELECT DEPTNO FROM dept WHERE DNAME = %s", (dept_dname2,))
        result = cursor.fetchone()
        if result:
            deptno2 = result[0]
        else:
            mb.showerror("Error", "Departamento no encontrado")
            return
        datos=(self.entry_ename2.get(),
               self.entry_job2.get(),
               mgr2,
               self.entry_hiredate2.get(),
               self.entry_sal2.get(),
               self.entry_comm2.get(),
               deptno2,
               self.entry_empno2.get())
        respuesta3=self.empleado.modificar(datos)
        if respuesta3>0:
            mb.showinfo("Información","Usuario actualizado existosamente")
        else:
            mb.showerror("Información","No se pudo modificar")


aplicacion1=Principal()
