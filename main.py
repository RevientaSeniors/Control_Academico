from os import sep, system
import re
from tkinter.filedialog import askopenfilename
from Alumno import Alumno

alumnosLista=[]
parametrosLista=[]
tituloCurso=""
promedioGlobal = 0
minimaGlobal = []
maximaGlobal = []
aprobadosGlobal = 0
reprobadosGlobal = 0
alumnosListaASC =[]
alumnosListaDESC=[]
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
    elif opcion == 3:
        if len(parametrosLista) !=0:
            exportarReporte()
        else:
            input("Debe cargar un archivo para acceder a esta opción")
            pintarMenu()
    elif opcion == 4:
        exit()
            
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
    global alumnosListaASC
    global alumnosListaDESC
    global promedioGlobal
    global maximaGlobal
    global minimaGlobal
    global aprobadosGlobal
    global reprobadosGlobal
    print("NOMBRE DEL CURSO: ", tituloCurso)
    print("ESTUDIANTES: ", len(listaAlumnos))
    print("-----------------PARAMETROS-----------------")
    ordenados = quicksortASC(listaAlumnos)
    alumnosListaASC =  ordenados
    alumnosListaDESC = list(reversed(ordenados))
    for parametro in ListaParametros:
        if parametro == "DESC":
            print(parametro)
            for i in alumnosListaDESC:
                print("Alumno: ",i.get_nombre()," Nota:",i.get_puntos())
            print("---------------------------------------------")
            
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
            promedioGlobal = round(promedio,2)
            print("El promedio de los alumnos es: ", round(promedio,2))
            print("---------------------------------------------")
            
        elif parametro == "MIN":
            print(parametro)
            print(ordenados[0].get_nombre()," obtuvo la nota más baja, con: ", ordenados[0].get_puntos()," puntos.")
            minimaGlobal = ordenados[0]
            print("---------------------------------------------")
        elif parametro == "MAX":
            print(parametro)
            print(ordenados[len(ordenados)-1].get_nombre()," obtuvo la nota más alta, con: ", ordenados[len(ordenados)-1].get_puntos()," puntos.")
            maximaGlobal = ordenados[len(ordenados)-1]
            print("---------------------------------------------")
        elif parametro == "APR":
            print(parametro)
            aprobados = 0
            for alumno in ordenados:
                if alumno.get_puntos() >= 61:
                    aprobados+=1
            print("Estudiantes aprobados: ", aprobados)
            aprobadosGlobal = aprobados
            print("---------------------------------------------")
              
            
        elif parametro == "REP":
            print(parametro)
            reprobados = 0
            for alumno in ordenados:
                if alumno.get_puntos() < 61:
                    reprobados+=1
            print("Estudiantes reprobados: ", reprobados)
            reprobadosGlobal = reprobados
            print("---------------------------------------------")
    input("PRESIONE ALGUNA TECLA PARA VOLVER AL MENÚ")
    pintarMenu()    


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

def exportarReporte():
    global tituloCurso
    global parametrosLista
    global alumnosListaASC
    global alumnosListaDESC

    documento = open("Control_Academico.html",'w')
    
    mensaje = """
    <!DOCTYPE html>
        <html lang="en">
            <head>
                <title> NOTAS </title>
            </head>
                <body>"""
    for parametro in parametrosLista:
        if parametro == "ASC":
                mensaje+="""
                    <h1> ASC </h1>
                    <table class="default" border="1">
                        <thead>
				            <tr>
					            <th colspan="2">""" +tituloCurso+ """</th>
				            </tr>
			            </thead>
                        <tr>
                            <th> ALUMNOS </th>
                            <th> NOTAS </th>
                        </tr>
                     """
                for alumno in alumnosListaASC:
                    mensaje += """
                        <tr>     
                            <td>"""+alumno.get_nombre()+""" </td>
                               """
                    if alumno.get_puntos()<61:
                        mensaje+="""
                            <td style="background-color: red;" style="color:#ff0000">"""+str(alumno.get_puntos())+"""</td>
                                """
                    else: 
                        mensaje+="""
                            <td style="background-color: blue;">"""+str(alumno.get_puntos())+"""</td>
                                """
                    mensaje+="""    
                        </tr>
                    """
                mensaje += """
                    </table>
                    """
        elif parametro == "DESC":
                mensaje+="""
                    <h1> DESC </h1>
                    <table class="default" border="1">
                        <thead>
				            <tr>
					            <th colspan="2">""" +tituloCurso+ """</th>
				            </tr>
			            </thead>
                        <tr>
                            <th> ALUMNOS </th>
                            <th> NOTAS </th>
                        </tr>
                     """
                for alumno in alumnosListaDESC:
                    mensaje += """
                        <tr>     
                            <td>"""+alumno.get_nombre()+""" </td>
                               """
                    if alumno.get_puntos()<61:
                        mensaje+="""
                            <td style="background-color: red;">"""+str(alumno.get_puntos())+"""</td>
                                """
                    else: 
                        mensaje+="""
                            <td style="background-color: blue;>"""+str(alumno.get_puntos())+"""</td>
                                """
                    mensaje+="""    
                        </tr>
                    """
                mensaje += """
                    </table>
                 """
        elif parametro == "AVG":
                mensaje+="""
                    <h1> AVG </h1>
                    <table class="default" border="1">
                        <thead>
				            <tr>
					            <th colspan="2"> PROMEDIO DE LOS ESTUDIANTES </th>
				            </tr>
			            </thead>
                        <tr>
                            <th>"""+str(promedioGlobal)+"""</th>
                        </tr>
                    </table>
                     """
        elif parametro == "MIN":
                mensaje+="""
                    <h1> MIN </h1>
                    <table class="default" border="1">
                        <thead>
				            <tr>
					            <th colspan="2"> NOTA MÍNIMA </th>
				            </tr>
			            </thead>
                        <tr>
                            <th>ALUMNO</th>
                            <th>NOTA</th>
                        </tr>
                        <tr>
                            <td>"""+minimaGlobal.get_nombre()+"""</td>
                            <td>"""+str(minimaGlobal.get_puntos())+"""</td>
                        </tr>
                    </table>
                     """
        elif parametro == "MAX":
                mensaje+="""
                    <h1> MAX </h1>
                    <table class="default" border="1">
                        <thead>
				            <tr>
					            <th colspan="2"> NOTA MÁXIMA </th>
				            </tr>
			            </thead>
                        <tr>
                            <th>ALUMNO</th>
                            <th>NOTA</th>
                        </tr>
                        <tr>
                            <td>"""+maximaGlobal.get_nombre()+"""</td>
                            <td>"""+str(maximaGlobal.get_puntos())+"""</td>
                        </tr>
                    </table>
                     """
        elif parametro == "APR":
                mensaje+="""
                    <h1> APR </h1>
                    <table class="default" border="1">
                        <thead>
				            <tr>
					            <th colspan="2"> ESTUDIANTES ARPOBADOS </th>
				            </tr>
			            </thead>
                        <tr>
                            <th>"""+str(aprobadosGlobal)+"""</th>
                        </tr>
                    </table>
                     """
        elif parametro == "REP":
                mensaje+="""
                    <h1> REP </h1>
                    <table class="default" border="1">
                        <thead>
				            <tr>
					            <th colspan="2"> ESTUDIANTES REPROBADOS </th>
				            </tr>
			            </thead>
                        <tr>
                            <th>"""+str(reprobadosGlobal)+"""</th>
                        </tr>
                    </table>
                     """
    mensaje += """       
                </body>
        </html>"""
    documento.write(mensaje)
    documento.close()
    input("REPORTE GENERADO EN HTML CORRECTAMENTE")
    pintarMenu()



if __name__ == '__main__':
    pintarMenu()