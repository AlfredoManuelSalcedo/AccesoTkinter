matriz=[
        {"texto":"CE" ,"estilo":"**estilo" , "funcion":"self.remplazarTexto('0')","row":1,"column":0},
        {"texto":"1/x","estilo":"**estilo" , "funcion":"self.inversa()","row":1,"column":2},
        {"texto":"Del","estilo":"**estilo" , "funcion":"self.borrarUltimoCaracter()","row":1,"column":1},
        {"texto":"0"  ,"estilo":"**estilo1", "funcion":"self.añadir('0')","row":5,"column":1},
        {"texto":"1"  ,"estilo":"**estilo1", "funcion":"self.añadir('1')","row":4,"column":0},
        {"texto":"2"  ,"estilo":"**estilo1", "funcion":"self.añadir('2')","row":4,"column":1},
        {"texto":"3"  ,"estilo":"**estilo1", "funcion":"self.añadir('3')","row":4,"column":2},
        {"texto":"4"  ,"estilo":"**estilo1", "funcion":"self.añadir('4')","row":3,"column":0},
        {"texto":"5"  ,"estilo":"**estilo1", "funcion":"self.añadir('5')","row":3,"column":1},
        {"texto":"6"  ,"estilo":"**estilo1", "funcion":"self.añadir('6')","row":3,"column":2},
        {"texto":"7"  ,"estilo":"**estilo1", "funcion":"self.añadir('7')","row":2,"column":0},
        {"texto":"8"  ,"estilo":"**estilo1", "funcion":"self.añadir('8')","row":2,"column":1},
        {"texto":"9"  ,"estilo":"**estilo1", "funcion":"self.añadir('9')","row":2,"column":2},
        {"texto":"/"  ,"estilo":"**estilo" , "funcion":"self.añadir('/')","row":1,"column":3},
        {"texto":"*"  ,"estilo":"**estilo" , "funcion":"self.añadir('*')","row":2,"column":3},
        {"texto":"-"  ,"estilo":"**estilo" , "funcion":"self.añadir('-')","row":3,"column":3},
        {"texto":"+"  ,"estilo":"**estilo" , "funcion":"self.añadir('+')","row":4,"column":3},
        {"texto":"+/-","estilo":"**estilo" , "funcion":"self.cambioSigno()","row":5,"column":0},
        {"texto":"."  ,"estilo":"**estilo" , "funcion":"self.añadir('.')","row":5,"column":2},
        {"texto":"="  ,"estilo":"**estilo" , "funcion":"self.evaluar()","row":5,"column":3}]

for a in matriz:
     print(a["texto"],a["estilo"],a["funcion"])

     import tkinter as tk
from tkinter import ttk
import mysql.connector

# Conectar a la base de datos MySQL (reemplaza los valores con los de tu configuración)
conn = mysql.connector.connect(
    host="tu_host",
    user="tu_usuario",
    password="tu_contraseña",
    database="tu_base_de_datos"
)
cursor = conn.cursor()

# Crear una tabla de ejemplo
cursor.execute("CREATE TABLE IF NOT EXISTS datos_ejemplo (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255))")
conn.commit()

# Insertar datos de ejemplo
cursor.execute("INSERT INTO datos_ejemplo (nombre) VALUES ('Dato 1')")
cursor.execute("INSERT INTO datos_ejemplo (nombre) VALUES ('Dato 2')")
cursor.execute("INSERT INTO datos_ejemplo (nombre) VALUES ('Dato 3')")
conn.commit()

# Consultar datos desde la base de datos
cursor.execute("SELECT nombre FROM datos_ejemplo")
datos = cursor.fetchall()

# Crear la interfaz gráfica con Tkinter
root = tk.Tk()
root.title("Combobox con Datos SQL")

# Variable de control para el Combobox
selected_data = tk.StringVar()

# Crear el Combobox y configurarlo con los datos de la consulta SQL
combobox = ttk.Combobox(root, textvariable=selected_data)
combobox['values'] = [dato[0] for dato in datos]
combobox.pack(pady=10)

def seleccionar():
    seleccionado = selected_data.get()
    print("Seleccionado:", seleccionado)

# Botón para obtener la selección
boton_seleccionar = tk.Button(root, text="Seleccionar", command=seleccionar)
boton_seleccionar.pack(pady=10)

root.mainloop()

# Cerrar la conexión a la base de datos al salir
conn.close()