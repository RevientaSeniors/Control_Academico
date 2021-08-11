from os import sep, system
import re
from tkinter.filedialog import askopenfilename
from Alumno import Alumno

alumnosLista=[]
parametrosLista=[]
tituloCurso=""
alumnosListaASC =[]
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
            mostrarReporteEnConsola(parametrosLista,alumnosLista,tituloCurso)
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
        analizar(contenido)
        pintarMenu()

def limpiarPantalla():
    system('cls')

#Parte logica del cual se separa el texto y se convierte en objetos de tipo Alumno
def analizar(contenido):
    global tituloCurso
    spliteado = re.split('{|}',contenido)
    specialCharsT = "_="
    titulo = spliteado[0]
    for specialCharT in specialCharsT:
        titulo = titulo.replace(specialCharT, " ")
    tituloCurso = titulo
    datosAlumno = spliteado[1].split(sep = ',')
    for i in range(len(datosAlumno)):
        dato = datosAlumno[i].split(sep=';')
        specialCharsA = '{<"'
        alumno = dato[0]
        for specialCharA in specialCharsA:
            alumno = alumno.replace(specialCharA,"")  
            alumno = alumno.strip()      
        nota = int(dato[1].replace(">","").strip())
        nuevoAlumno = Alumno(alumno,nota)
        alumnosLista.append(nuevoAlumno)
    parametros = spliteado[2].split(sep=",")
    for i in range(len(parametros)):
        parametro = parametros[i].strip()
        parametrosLista.append(parametro)

    
    

def  mostrarReporteEnConsola(ListaParametros,listaAlumnos,tituloCurso):
    print("NOMBRE DEL CURSO: ", tituloCurso)
    print("-----------------PARAMETROS-----------------")
    ordenados = quicksortASC(listaAlumnos)
    for parametro in ListaParametros:
        if parametro == "DESC":
            parametroDESC(listaAlumnos)
            
        elif parametro == "ASC":
            print(parametro)
            for i in ordenados:
                print("Alumno: ",i.get_nombre()," Nota:",i.get_puntos())
            print("---------------------------------------------")
            
        elif parametro == "AVG":
            print(parametro)
            sumaNotas =0
            for alumno in ordenados:
                sumaNotas += alumno.get_puntos()
            promedio = sumaNotas/len(ordenados)
            print("El promedio de los alumnos es: ", round(promedio,2))
            print("---------------------------------------------")
            
        elif parametro == "MIN":
            print(parametro)
            print(ordenados[0].get_nombre()," obtuvo la nota más baja, con: ", ordenados[0].get_puntos()," puntos.")
            print("---------------------------------------------")
        elif parametro == "MAX":
            print(parametro)
            print(ordenados[len(ordenados)-1].get_nombre()," obtuvo la nota más alta, con: ", ordenados[len(ordenados)-1].get_puntos()," puntos.")
            print("---------------------------------------------")
        elif parametro == "APR":
            print(parametro)
            aprobados = 0
            for alumno in ordenados:
                if alumno.get_puntos() >= 61:
                    aprobados+=1
            print("Estudiantes aprobados: ", aprobados)
            print("---------------------------------------------")
              
            
        elif parametro == "REP":
            print(parametro)
            reprobados = 0
            for alumno in ordenados:
                if alumno.get_puntos() < 61:
                    reprobados+=1
            print("Estudiantes reprobados: ", reprobados)
            print("---------------------------------------------")
            


def parametroDESC(listaAlumnos):
    print("DESC")

def parametroASC(listaAlumnos):
    pivote = listaAlumnos[0]
    menores=[]
    mayores =[]

    for i in range(1,len(listaAlumnos)):
        if listaAlumnos[i].get_puntos() < pivote.get_puntos():
            menores.append(listaAlumnos[i])
        else:
            mayores.append(listaAlumnos[i])
    return menores,pivote,mayores

def quicksortASC(listaAlumnos):
    if len(listaAlumnos)<2:
        return listaAlumnos
    menores,pivote,mayores = parametroASC(listaAlumnos)

    return quicksortASC(menores)+[pivote]+quicksortASC(mayores)






if __name__ == '__main__':
    pintarMenu()