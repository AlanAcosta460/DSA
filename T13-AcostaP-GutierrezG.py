alumnos = { # Diccionario de datos de alumnos (variable global)
        1: [((20), ["lun", "mie"]), ((21),["mar","jue"]), ((28),["lun","mie", "vie"])],
        2: [((20), ["mar", "jue"]), ((23),["mie","vie"]), ((27),["mie","jue", "vie"])],
        3: [((21), ["mie", "vie"]), ((24),["jue"]), ((28),["lun","vie"])],
        4: [((20), ["mie"]), ((21),["jue","vie"]), ((23),["lun","mie"])]
}

def show_claves_materias(n):
    for i in alumnos[n]:
        print("Clave: ", i[0], end="\t")
        print("Dias: ", end="")
        for j in i[1]:
            print(j, end=", ")
        print()

def pedir_num_cuenta(): # Pide el numero de cuenta de un alumno
    while True:
        n = int(input("Ingrese el numero de cuenta del alumno: "))
        if n in alumnos:
            return n
        else:
            print("No existe ese numero de cuenta\n")
    
def buscar(): # Muestra las claves de las materias de un alumno y si tiene clases el martes 
    n = pedir_num_cuenta()

    print("\n\t**** Horario ****")
    show_claves_materias(n)

    for i in range(0, 3):
        if "mar" in alumnos[n][i][1]:
            print("\nTiene clases el martes\n")
            return
    print("\nNo tiene clases el martes\n")
    
def eliminar_materia(): # Elimina la clave de una materia
    n = pedir_num_cuenta()

    print("\n\t**** Horario ****")
    show_claves_materias(n)
    
    clave = int(input("\nIngrese la clave de la materia que desea eliminar: "))
    if clave not in alumnos[n][0] and clave not in alumnos[n][1] and clave not in alumnos[n][2]:
        print("No existe esa clave\n")
        return

    print(f"\nEsta seguro que desea eliminar la materia {clave}?")
    print("(1) -- Si\n(2) -- No")
    while True:
        opcion = int(input("\nIngrese una opcion: "))
        if opcion == 1 or opcion == 2:
            break
        else:
            print("Opcion invalida")

    if opcion == 1:
        for i in alumnos[n]:
            if i[0] == clave:
                alumnos[n].remove(i)
                print("\nSe elimino la materia\n")
    else:
        print("\nNo se elimino la materia\n")

def eliminar_alumno(): # Elimina todos los datos de relacionados a un alumno
    n = pedir_num_cuenta()

    print(f"\nEsta seguro que desea eliminar al alumno {n}?")
    print("(1) -- Si\n(2) -- No")
    while True:
        opcion = int(input("\nIngrese una opcion: "))
        if opcion == 1 or opcion == 2:
            break
        else:
            print("Opcion invalida")

    if opcion == 1:
        del alumnos[n]
        print("\nSe elimino al alumno\n")
    else:
        print("\nNo se elimino al alumno\n")

def mod_dia(): # Modifica un dia de una materia
    n = pedir_num_cuenta()

    print("\n\t**** Horario ****")
    show_claves_materias(n)
    
    clave = int(input("\nIngrese la clave de la materia: "))
    if clave not in alumnos[n][0] and clave not in alumnos[n][1] and clave not in alumnos[n][2]:
        print("No existe esa clave\n")
        return

    dia = input("\nIngrese el dia que desea modificar: ")
    for i in alumnos[n]:
        if i[0] == clave:
            if dia not in i[1]:
                print("No existe ese dia\n")
                return

    print(f"\nEsta seguro que desea modificar el dia {dia}?")
    print("(1) -- Si\n(2) -- No")
    while True:
        opcion = int(input("\nIngrese una opcion: "))
        if opcion == 1 or opcion == 2:
            break
        else:
            print("Opcion invalida")

    if opcion == 1:
        for i in alumnos[n]:
            if i[0] == clave:
                i[1].remove(dia)
                i[1].append(input("\nIngrese el nuevo dia: "))
                print("Se modifico el dia\n")
    else:
        print("No se modifico el dia\n")

def agregar_alu(): # Pide los datos de un alumno y los agrega al diccionario
    n = int(input("Ingrese el numero de cuenta del alumno: "))
    if n in alumnos:
        print("Ya existe ese numero de cuenta\n")
        return
    
    if n < 1 or n > 10:
        print("Numero de cuenta invalido\n")
        return 
    
    alumnos[n] = []
    for i in range(0, 3):
        while True:
            clave = int(input("\nIngrese la clave de la materia que desea agregar: "))
            if clave < 20 and clave > 30:
                print("Clave invalida")
            else:
                break
        dias = input("Ingrese los dias de la materia separados por comas: ").split(",")
        alumnos[n].append((clave,dias))
    print("\nSe agrego el alumno\n")   

def show_diccionario(): # Muestra el diccionario completo con formato
    for i in alumnos:
        print("Numero de cuenta: ", i)
        show_claves_materias(i)
        print()

def main():
    while True: 
        print("\t*** MENU ***")
        print("(1) -- Buscar por numero de cuenta")
        print("(2) -- Eliminar la clave de una materia")
        print("(3) -- Eliminar un alumno")   
        print("(4) -- Modificar la lista de dias para una materia")
        print("(5) -- Agregar un alumno")
        print("(6) -- Mostrar diccionario completo")
        print("(7) -- Salir")

        while True:
            opcion = int(input("\nIngrese una opcion: "))
            if opcion >= 1 and opcion <= 7:
                break
            else:
                print("Opcion invalida")
        print()
 
        if opcion == 1:
            buscar()
        elif opcion == 2:
            eliminar_materia()
        elif opcion == 3:
            eliminar_alumno()
        elif opcion == 4:
            mod_dia()
        elif opcion == 5:
            agregar_alu()
        if opcion == 6:
            show_diccionario()
        if opcion == 7:
            break

if __name__ == '__main__':
    main()
