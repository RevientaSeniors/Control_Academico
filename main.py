from os import system
from tkinter.filedialog import askopenfilename

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

def cargarArchivo():
    fileName = askopenfilename()
    archivo = open(fileName, 'r')
    contenido = archivo.read()
    archivo.close()
    print("CONTENIDO CARGADO CON EXITO, ¿DESEA VER EL CONTENIDO? (Y/N)" , end="")
    respuesta = input()
    if respuesta  == 'Y':
        analizar(contenido)
        #print(contenido)
        #pintarMenu()
    elif respuesta == 'N':
        pintarMenu()

def limpiarPantalla():
    system('cls')

def analizar(contenido):
    spliteado = contenido.split(sep = '=')
    titulo = spliteado[0].replace("_", " ")
    print("NOMBRE DEL CURSO: ", titulo)


if __name__ == '__main__':
    pintarMenu()