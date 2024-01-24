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