from os import sep, system
import re
from tkinter.filedialog import askopenfilename
from Alumno import Alumno

alumnosLista=[]
parametrosLista=[]
def pintarMenu():
    limpiarPantalla()
    print("────────────── MENÚ ────────────── ")
    print("│ 1. CARGAR ARCHIVO               │")
    print("│ 2. MOSTRAR REPORTE EN CONSOLA   │")
    print("│ 3. EXPORTAR REPORTE             │")
    print("│ 4. SALIR                        │")
    print("───────────────────────────────────")
    opcion = int(input())
    if opcion == 1:
        limpiarPantalla()
        cargarArchivo()   
    elif opcion == 2:
        if len(parametrosLista) != 0:
            recibirParametros(parametrosLista)
        else:
            input("Debe cargar un archivo para acceder a esta opción")
            pintarMenu()

            
def cargarArchivo():
    fileName = askopenfilename()
    archivo = open(fileName, 'r')
    contenido = archivo.read()
    archivo.close()
    print("CONTENIDO CARGADO CON EXITO, ¿DESEA VER EL CONTENIDO? (Y/N)" , end="")
    respuesta = input()
    if respuesta  == 'Y':
        analizar(contenido)
        print(contenido)
        pintarMenu()
    elif respuesta == 'N':
        pintarMenu()

def limpiarPantalla():
    system('cls')

#Parte logica del cual se separa el texto y se convierte en objetos de tipo Alumno
def analizar(contenido):
    spliteado = re.split('{|}',contenido)
    specialCharsT = "_="
    titulo = spliteado[0]
    for specialCharT in specialCharsT:
        titulo = titulo.replace(specialCharT, " ")
    print("NOMBRE DEL CURSO: ", titulo)
    datosAlumno = spliteado[1].split(sep = ',')
    
    print("Alumnos:")
    for i in range(len(datosAlumno)):
        dato = datosAlumno[i].split(sep=';')
        specialCharsA = '{<"'
        alumno = dato[0]
        for specialCharA in specialCharsA:
            alumno = alumno.replace(specialCharA,"")  
            alumno = alumno.strip()      
        nota = dato[1].replace(">","").strip()
        nuevoAlumno = Alumno(alumno,nota)
        alumnosLista.append(nuevoAlumno)
        
    
    parametros = spliteado[2].split(sep=",")
    for i in range(len(parametros)):
        parametro = parametros[i].strip()
        parametrosLista.append(parametro)
    
    

def recibirParametros(ListaParametros):
    print("Estamos dentro del metodo")
    print(ListaParametros)


if __name__ == '__main__':
    pintarMenu()