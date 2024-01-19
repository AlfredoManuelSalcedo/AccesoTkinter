import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb 
from tkinter import scrolledtext as st 
import socio

class FormularioSocios:
    def __init__(self):
        self.socio=socio.Socio()
        self.ventana1=tk.Tk()
        self.ventana1.title("Socios de baloncesto")

        self.ventana1.resizable(False,False)
        self.ventana1.configure(background="#6A9F80")
        w=525
        h = 400
        x=(self.ventana1.winfo_screenwidth() / 2) - (w/2)
        y = (self.ventana1.winfo_screenheight()/2)-(h/2)
        self.ventana1.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.cuaderno1 = ttk.Notebook(self.ventana1)
        self.Insertar()
        self.consultaSocio()
        self.listado_completo()
        self.borrado()
        self.cuaderno1.grid(column=0, row=0, padx=10,pady=10)
        self.ventana1.mainloop()

    #<<<<<<<<<<<<<<<<<<<<<INSERTAR>>>>>>>>>>>>>>>>>>>>>>>
    def Insertar(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Insertar socio")

        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Socio")
        self.labelframe1.grid(column=0,row=0,padx=5,pady=10)

        #====================socioID=====================#
        self.label1=ttk.Label(self.labelframe1, text="socioID:")
        self.label1.grid(column=0,row=0,padx=4,pady=4)

        self.socioID=tk.IntVar()
        self.entrysocioID=ttk.Entry(self.labelframe1,textvariable=self.socioID)
        self.entrysocioID.grid(column=1,row=0,padx=4,pady=4)

        #====================nombre=====================#
        self.label2=ttk.Label(self.labelframe1, text="Nombre:")
        self.label2.grid(column=0, row=1,padx=4,pady=4)

        self.nombre=tk.StringVar()
        self.entrynombre=ttk.Entry(self.labelframe1,textvariable=self.nombre)
        self.entrynombre.grid(column=1,row=1,padx=4,pady=4)

        #====================estatura=====================#
        self.label3=ttk.Label(self.labelframe1, text="Estatura:")
        self.label3.grid(column=0, row=2,padx=4,pady=4)

        self.estatura=tk.IntVar()
        self.entryestatura=ttk.Entry(self.labelframe1,textvariable=self.estatura)
        self.entryestatura.grid(column=1,row=2,padx=4,pady=4)

        #====================edad=====================#
        self.label4=ttk.Label(self.labelframe1, text="Edad:")
        self.label4.grid(column=0, row=3,padx=4,pady=4)

        self.edad=tk.IntVar()
        self.entryedad=ttk.Entry(self.labelframe1,textvariable=self.edad)
        self.entryedad.grid(column=1,row=3,padx=4,pady=4)

        #====================localidad=====================#
        self.label5=ttk.Label(self.labelframe1, text="Localidad:")
        self.label5.grid(column=0, row=4,padx=4,pady=4)

        self.localidad=tk.StringVar()
        self.entrylocalidad=ttk.Entry(self.labelframe1,textvariable=self.localidad)
        self.entrylocalidad.grid(column=1,row=4,padx=4,pady=4)

        #====================boton=====================#
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.BInsertar)
        self.boton1.grid(column=1,row=5,padx=4,pady=4)

    def BInsertar(self):
        datos=(self.socioID.get(), self.nombre.get(),self.estatura.get(),self.edad.get(),self.localidad.get())
        self.socio.nuevo_socio(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.socioID.set("")
        self.nombre.set("")
        self.estatura.set("")
        self.edad.set("")
        self.localidad.set("")

    #<<<<<<<<<<<<<<<<<<<<<CONSULTAR>>>>>>>>>>>>>>>>>>>>>>>
    def consultaSocio(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta")
    
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Busqueda:")
        self.labelframe2.grid(column=0,row=0,padx=5,pady=10)

        #====================socioID=====================#
        self.label6=ttk.Label(self.labelframe2, text="socioID:")
        self.label6.grid(column=0,row=0,padx=4,pady=4)

        self.socioID2=tk.IntVar()
        self.entrysocioID2=ttk.Entry(self.labelframe2,textvariable=self.socioID2)
        self.entrysocioID2.grid(column=1,row=0,padx=4,pady=4)

        #====================nombre=====================#
        self.label7=ttk.Label(self.labelframe2, text="Nombre:")
        self.label7.grid(column=0, row=1,padx=4,pady=4)

        self.nombre2=tk.StringVar()
        self.entrynombre2=ttk.Entry(self.labelframe2,textvariable=self.nombre2, state="readonly")
        self.entrynombre2.grid(column=1,row=1,padx=4,pady=4)

        #====================estatura=====================#
        self.label8=ttk.Label(self.labelframe2, text="Estatura:")
        self.label8.grid(column=0, row=2,padx=4,pady=4)

        self.estatura2=tk.IntVar()
        self.entryestatura2=ttk.Entry(self.labelframe2,textvariable=self.estatura2, state="readonly")
        self.entryestatura2.grid(column=1,row=2,padx=4,pady=4)

        #====================edad=====================#
        self.label9=ttk.Label(self.labelframe2, text="Edad:")
        self.label9.grid(column=0, row=3,padx=4,pady=4)

        self.edad2=tk.IntVar()
        self.entryedad2=ttk.Entry(self.labelframe2,textvariable=self.edad2, state="readonly")
        self.entryedad2.grid(column=1,row=3,padx=4,pady=4)

        #====================localidad=====================#
        self.label10=ttk.Label(self.labelframe2, text="Localidad:")
        self.label10.grid(column=0, row=4,padx=4,pady=4)

        self.localidad2=tk.StringVar()
        self.entrylocalidad2=ttk.Entry(self.labelframe2,textvariable=self.localidad2, state="readonly")
        self.entrylocalidad2.grid(column=1,row=4,padx=4,pady=4)

         #====================boton=====================#
        self.boton2=ttk.Button(self.labelframe2, text="Buscar", command=self.Consultar)
        self.boton2.grid(column=1,row=5,padx=4,pady=4)

    def Consultar(self):
        datos=(self.socioID2.get(),)
        respuesta=self.socio.consultaSocio(datos)
        if len(respuesta)>0:
            self.nombre2.set(respuesta[0][0])
            self.estatura2.set(respuesta[0][1])
            self.edad2.set(respuesta[0][2])
            self.localidad2.set(respuesta[0][3])
        else:
            self.nombre2.set("")
            self.estatura2.set("")
            self.edad2.set("")
            self.localidad2.set("")
            mb.showerror("Información", "No existe un socio con dicho codigo")


    #<<<<<<<<<<<<<<<<<<<<<LISTAR>>>>>>>>>>>>>>>>>>>>>>>
    def listado_completo(self):
        self.pagina3=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")

        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Socio")
        self.labelframe3.grid(column=0,row=0,padx=5,pady=10)
   
        self.boton3=ttk.Button(self.labelframe3, text="Listado completo", command=self.listar)
        self.boton3.grid(column=0,row=0,padx=4,pady=4)

        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0, row=1,padx=10,pady=10)
    
    def listar(self):
        respuesta=self.socio.socios()
        self.scrolledtext1.delete("1.0", tk.END)
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "socioID:"+str(fila[0])+
                                              "\nNombre:"+fila[1]+
                                              "\nEstatura:"+str(fila[2])+
                                              "\nEdad:"+str(fila[3])+
                                              "\nLocalidad:"+str(fila[4])+
                                              "\n\n")
    
    #<<<<<<<<<<<<<<<<<<<<<<<<<BORRAR>>>>>>>>>>>>>>>>>>>>>>>
    def borrado(self):
        self.pagina4=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Borrado de socios")

        self.labelframe4=ttk.LabelFrame(self.pagina4, text="Socio")
        self.labelframe4.grid(column=0,row=0,padx=5,pady=10)

        self.label11=ttk.Label(self.labelframe4, text="socioID:")
        self.label11.grid(column=0, row=0,padx=4,pady=4)

        self.codigoborra=tk.StringVar()
        self.entrycodigoborra=ttk.Entry(self.labelframe4,textvariable=self.codigoborra)
        self.entrycodigoborra.grid(column=1,row=0,padx=4,pady=4)

        self.boton4=ttk.Button(self.labelframe4, text="Borrar", command=self.borrar)
        self.boton4.grid(column=1,row=1,padx=4,pady=4)

    def borrar(self):
        datos=(self.codigoborra.get(),)
        cantidad=self.socio.borrar_socio(datos)
        if cantidad==1:
            mb.showinfo("Información", "Socio eliminado")
            self.codigoborra.set("")
        else:
            mb.showerror("Información", "No existe un articulo con dicho codigo")

aplicacion1=FormularioSocios()

        



