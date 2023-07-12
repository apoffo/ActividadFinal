'''
listado de 20 alumnos con nombres completos
y notas numéricas entre 3 y 6 notas
'''
import time

def menu():
    print("\n")
    print ("a) Mostrar la lista ordenada de alumnos.")
    print ("b) Mostrar la lista ordenada de alumnos con sus notas.")
    print ("c) Mostrar la lista ordenada de alumnos con sus promedios.")
    print ("d) Mostrar la nota media de todos los alumnos.")
    print ("e) Mostrar la nota media de los alumnos aprobados.")
    print ("f) Mostrar la nota media de los alumnos suspendidos.")
    print ("g) Salir del programa")
    opcion = input("Elija una opción de las que verá a continuación: ")
    return opcion.lower()
    print("\n")
#********************************************************************************
#a
def lista_ordenada_alumnos(alumnos): #filtro por llave que muestra solo los nombres
    #print("opcion a")
    for alumno in sorted(alumnos): 
        print(alumno)
    print("\n")

#***********************************************************************************************
#b
def lista_ordenada_alumnos_con_notas(alumnos): #filtro por llave y valor para que muestre ambos
    #print("opcion b")
    for alumno in sorted(alumnos):
        notas = alumnos[alumno] #recupero el valor de las notas, la lista de notas
        print(f"{alumno}: {notas}")
    print("\n")
        
#************************************************************************************************
#c
def lista_ordenada_alumnos_con_promedios(alumnos): #filtro por valor y saco promedio
    #print("opcion c")
    for alumno in sorted(alumnos):
        notas = alumnos[alumno]
        promedio = sum(notas) / len(notas) #uso la función sum() para sumar la lista y len() para saber la cantidad de notas que tiene la lista
        print(f"{alumno}: promedio: {round(promedio, 2)}")
    print("\n")

    
#*************************************************************************************************
#d
def nota_media_alumnos(alumnos):
    #print("opcion d")
    todas_las_notas = [] #defino una lista donde voy a guardar todas las notas de todos los alumnos
    for notas in alumnos.values():
        todas_las_notas.extend(notas)
    #print(todas_las_notas)
    promedio_notas = sum(todas_las_notas) / len(todas_las_notas)
    print(f"El promedio de todas las notas es de {round(promedio_notas, 2)}.")
    print("\n")


#***************************************************************************************************
#e
def nota_media_alumnos_aprobados(alumnos):
    #print("opcion e")
    notas_alumnos_aprobados = [] #defino una lista donde voy a guardar todas las notas de todos los alumnos
    for notas in alumnos.values():
        promedio = sum(notas) / len(notas) 
        if promedio >= 6:
            notas_alumnos_aprobados.append(promedio)
    if notas_alumnos_aprobados:
        promedio_notas_aprobadas = sum(notas_alumnos_aprobados) / len(notas_alumnos_aprobados)
        print(f"El promedio de todas las notas de alumnos probados es de {round(promedio_notas_aprobadas, 2)}.")
    else:
        print("No hay alumnos aprobados.")
    print("\n")
    

#***********************************************************************************************************
#f
def nota_media_alumnos_suspendidos(alumnos):
    #print("opcion f")
    notas_alumnos_suspendidos = [] #defino una lista donde voy a guardar todas las notas de todos los alumnos
    for notas in alumnos.values():
        promedio = sum(notas) / len(notas) 
        if promedio < 6:
            notas_alumnos_suspendidos.append(promedio)
    if notas_alumnos_suspendidos:
        promedio_notas_suspendidos = sum(notas_alumnos_suspendidos) / len(notas_alumnos_suspendidos)
        print(f"El promedio de todas las notas de alumnos suspendidos es de {round(promedio_notas_suspendidos, 2)}.")
    else:
        print("No hay alumnos suspendidos.")
    print("\n")

    
#**********************************************************************************************************


print("Instituto Bilingüe Sagrada Familia")
print("Bienvenido/a profesor/a. A cargar notas se ha dicho! Suerte!")
time.sleep(2)
print("A continuación debe cargar los/as alumnos/as y las notas para luego poder filtrar según el menú de opciones.")
time.sleep(2)

cantidad_alumnos = int(input("Ingrese la cantidad de alumnos de su clase: "))
alumnos = {} #inicializo el diccionario

for i in range(cantidad_alumnos):
    notas =[] #defino la lista

    nombre_alumno = input("Ingrese el nombre completo del alumno: ")
    cant_notas = int(input("Ingrese la cantidad de notas (entre 3 y 6): "))

    while cant_notas < 3 or cant_notas > 6:
        print("Debe ingresar una cantidad mínima de 3 o máxima de 6 notas.")
        cant_notas = int(input("Ingrese la cantidad de notas (entre 3 y 6): "))

    for i in range(cant_notas):
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        notas.append(nota)
        
    alumnos[nombre_alumno] = notas #cargo el diccionario con la llave nombre y el valor de la lista notas
    print("\n")

opcion = menu()
while opcion != "g":
    if opcion == "a":
        print("\n")
        print("Lista ordenada de alumnos")
        lista_ordenada_alumnos(alumnos)
    elif opcion == "b":
        print("\n")
        print("Lista ordenada de alumnos con las notas")
        lista_ordenada_alumnos_con_notas(alumnos)
    elif opcion == "c":
        print("\n")
        print("Lista ordenada de promedios de alumnos")
        lista_ordenada_alumnos_con_promedios(alumnos)
    elif opcion == "d":
        print("\n")
        print("Notas promedio")
        nota_media_alumnos(alumnos)
    elif opcion == "e":
        print("\n")
        print("Promedio de notas de alumnos aprobados")
        nota_media_alumnos_aprobados(alumnos)
    elif opcion == "f":
        print("\n")
        print("Promedio de notas de alumnos desaprobados")
        nota_media_alumnos_suspendidos(alumnos)
    else:
        print("Opcion inválida. Elija una opción válida")
    opcion = menu()
    
print("Usted ha salido del programa. Hasta luego.")









    
