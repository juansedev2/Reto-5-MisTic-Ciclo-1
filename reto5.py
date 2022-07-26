"""
RETO 5:
Leer un archivo.csv que contiene una gran cantidad de registros, donde lo que debemos hacer es lo realizado en el análisis,
se puede ver en el archivo que hay 10 columnas y 100.000 filas. La primera corresponde a los títulos de la columna y el resto
a los registros. Debo de encontrar la forma de realizar el análisis y las operaciones sobre la data
"""

# Vamos a importar la libreria de Python CSV para facilidad de trabajo
import csv as csv

# import os  # Libreria para ver información y funciones del sistema operativo como el entorno

"""
Funcion para conocer el contexto de mi área de trabajo, lo usé para ver si localizaba mi
archivo csv
(ASEGURARSE EN VS CODE QUE SE EJECUTE DENTRO DEL CONTEXTO DEL TRABAJO (directorio real del módulo))
def infoContexto():

    global os
    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    print("Files in %r: %s" % (cwd, files))
"""

# Esta función leerá y devolverá la matriz con toda la data ya obtenida del archivo


def leerArchivo(ruta_archivo):

    try:  # Aprendamos a capturar excepciones en Python y prevenir fallos que detengan el programa

        # Apertura del archivo con la función open y en modo lectura con r
        with open(ruta_archivo, "r") as archivo:

            # Función reader de csv que facilita la lectura del archivo csv
            lector = csv.reader(archivo, delimiter=",",
                                quotechar=",", quoting=csv.QUOTE_MINIMAL)
            i = 0  # Solo para limitar y observar en testing de captura de datos
            matriz = []  # Guardaremos los datos en una matriz

            for registro in lector:

                """PARA PRUEBAS
                # print(regisro)
                # tipo = type(fila)  Ahora sabemos que el tipo de dato es lista
                #print(f"Es de tipo {tipo}")
                i += 1 EN PRUEBAS USAR VALIDACION DE i == 1 PARA CONTAR de manera "humana" las filas
                if i == 1:  # El primero registro son los títulos de las columnas, no lo necesitamos
                    continue
                elif i == 80000:  # Vamos a limitar a 500 solo para pruebas, luego eliminar esta condicion
                    break
                """
                if i == 0:  # El primero registro son los títulos de las columnas, no lo necesitamos

                    i += 1
                    continue

                matriz.append(registro)

            archivo.close()  # Es importante para liberar memoria porque el archivo ya no lo usaré

            return matriz

    except:  # En caso de no encontrar el archivo que se le pase

        print("No existe el archivo, verifique la ruta y/o revise otros errores")


# Función para saber si a un paciente se le programa o nó la entrega de medicamentos
def programarEntrega(p_sistolica, p_distolica):

    if p_sistolica < 91 and p_distolica < 63:  # Categoría de Hipontesión

        return True

    elif ((p_sistolica >= 91 and p_sistolica < 134) and (p_distolica >= 63 and p_distolica < 77)):  # Categoría de ideal

        return False

    elif((p_sistolica >= 134 and p_sistolica < 162) and (p_distolica >= 77 and p_distolica < 105)):  # Categoría de Normal

        return False

    elif((p_sistolica >= 162 and p_sistolica < 188) and (p_distolica >= 105 and p_distolica < 119)):  # Categoría de Normal - Alta

        return True

    elif((p_sistolica >= 188 and p_sistolica < 201) and (p_distolica >= 119 and p_distolica < 126)):  # Categoría de HTA Grado 1

        return True

    elif((p_sistolica >= 201 and p_sistolica < 214) and (p_distolica >= 126 and p_distolica < 146)):  # Categoría de HTA Grado 2

        return True

    elif(p_sistolica >= 214 and p_distolica >= 146):  # Categoría de HTA Grado 3

        return True

    elif(p_sistolica >= 152 and p_distolica < 77):  # Categoría de Hipertensión Solo Sistólica

        return True

    else:  # Pues en caso de ninguno, porque puede darse

        return False


# Función para obtener el resumen de la sucursal indicada
def imprimirInfoSucursal(sucursal, matriz):

    # Necesito obtener cada lista (registro) de la matriz y ver sus características

    i = 1  # Iterador para obtener ciudad y departamento
    hombres = 0  # Cantidad de hombres a los que se les programa medicamentos en la sucursal indicada
    mujeres = 0  # Cantidad de mujeres a los que se les programa medicamentos en la sucursal indicada
    cant_atendidos = 0  # Cantidad de pacientes a los cuales se atienden
    # Cantidad PROMEDIO de medicamentos programados SOLO para la sucursal indicada
    promedio_med_entregas = 0
    # Cantidad de medicamentos programados para la entrega (acumulador grande)
    total_medicamentos = 0
    ciudad_sucursal = ""  # Ciudad de la sucursal indicada
    departamento_sucursal = ""  # Departamento de la sucursal indicada

    for fila in matriz:

        """Partiendo que desde la posicion 0 es el nombre, entonces el cada avance es un dato
        distinto hasta 9
               # print(fila[0]) El nombre
               # print(fila[2]) El género
        Por lo tanto:
        nombre = fila[0]
        apellido = fila[1]
        genero = fila[2]
        ciudad = fila[3]
        departamento = fila[4]
        id_sucursal = fila[5]
        tipo_medicamento = fila[6]
        cantidad_solicitada = fila[7]  # Cantidad de medicamentos
        p_sistolica = fila[8]  # Presión sistólica
        p_distolica = fila[9]  # Presión distólica
        """
        # OJO CON LOS TIPOS DE DATOS, HAY QUE OBTENERLOS
        # Por lo tanto, lo primero sería validad la sucursal que me están solicitando
        if int(fila[5]) == sucursal:

            if i == 1:  # A partir del primer registro puedo obtener la ciudad y el departamento

                ciudad_sucursal = fila[3]
                departamento_sucursal = fila[4]
                i += 1

            # Contar a cuantos pacientes se les programa la cantidad de medicamentos
            if programarEntrega(int(fila[8]), int(fila[9])):  # En caso de ser True, es que es se programa el medicamento

                 # Contar cuantas mujeres y hombres son
                if fila[2] == "m":
                    hombres += 1
                elif fila[2] == "f":
                    mujeres += 1

                cant_atendidos += 1  # Un paciente más es atendido
                total_medicamentos += int(fila[7])  # Se acumula la cantidad de medicamentos que se solicita

    # Una vez completado todos los datos anteriores, ya podemos sacar el promedio
    # Y validamos POR SI ACASO:
    if cant_atendidos != 0:
        promedio_med_entregas = total_medicamentos / cant_atendidos
    else:
        promedio_med_entregas = 0

    #De una vez podemos proceder a mostrar los resultados
    print(f"{sucursal} {ciudad_sucursal} {departamento_sucursal}")  # Imprimir el id de la sucursal, ciudad y departamento
    print("scheduled patients")  # Pacientes a programar
    print(f"male {hombres}")  # Cantidad de hombres atendidos
    print(f"female {mujeres}")  # Cantidad de mujeres atendidos
    print(f"total {cant_atendidos}")  # El total de pacientes atendidos  # Es la suma de hombres y mujeres (NOTA: Usé el contador con el fin de validar el algoritmo y que si cuente los pacientes)
    print("scheduled medicine quantity")  # Programación de medicamentos
    print(f"mean {promedio_med_entregas:.2f}")  # Promedio de medicamentos entregados (redondeado a 2 cifras)
    print(f"total {total_medicamentos}")  # El total de medicamentos


# Main
def main():

    # Ruta del archivo
    ruta_archivo = "data.csv"  # Está en el mismo contexto de ruta, así que debería tomarlo
    matriz = leerArchivo(ruta_archivo)
    # Ahora que tengo la matriz, debo iniciar el procesamiento de la información
    #print("Digite la sucursal de la cual desea obtener el análisis de la información")
    sucursal = int(input())
    imprimirInfoSucursal(sucursal, matriz)


"""En resumen:
Esta estructura condicional me permite controlar mi programa en el sentido de saber que se está ejecutando, es decir, si yo
estoy ejecutando mi main (este módulo) o se ejecuta una importación (otro módulo), porque de lo contrario, ambas cosas se
ejecutarían (ambos módulos se ejecutan con lo que tengan) y eso no es bueno"""

if __name__ == '__main__':

    main()
    # infoContexto()
    #print("Entré al Main")
