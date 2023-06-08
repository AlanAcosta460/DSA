alumnos = {
        1: [((20), ["lun", "mie"]), ((21),["mar","jue"]), ((28),["lun","mie", "vie"])],
        2: [((20), ["mar", "jue"]), ((23),["mie","vie"]), ((27),["mie","jue", "vie"])],
        3: [((21), ["mar", "vie"]), ((24),["jue"]), ((28),["lun","vie"])],
        4: [((20), ["mie"]), ((21),["mar","jue"]), ((23),["lun","mie"])]
}
    
def buscar():
    n = int(input("Ingrese un numero de cuenta: "))
    if n in alumnos: 
        print("Claves de materias: ")
        for i in alumnos[n]:
            print("- ",i[0])
        if "mar" in alumnos[n][0][1] or "mar" in alumnos[n][1][1] or "mar" in alumnos[n][2][1]:
            print("Tiene clases el martes")
        else: 
            print("No tiene clases el martes")
    else:
        print("No existe ese numero de cuenta")
    print()
    
def eliminar_materia():
    n = int(input("Ingrese el numero de cuenta: "))
    if n in alumnos:
        print("Claves de materias: ")
        for i in alumnos[n]:
            print("- ",i[0])
        clave = int(input("Ingrese la clave de la materia que desea eliminar: "))
        for i in alumnos[n]:
            if i[0] == clave:
                alumnos[n].remove(i)
                print("Se elimino la materia")
    else:
        print("No existe ese numero de cuenta")
    print()

def eliminar_alumno():
    n = int(input("Ingrese el numero de cuenta: "))
    if n in alumnos:
        del alumnos[n]
        print("Se elimino al alumno")
    else:
        print("No existe ese numero de cuenta")
    print()

def mod_dia():
    n = int(input("Ingrese el numero de cuenta: "))
    if n in alumnos:
        print("Claves de materias: ")
        for i in alumnos[n]:
            print("- ",i[0])
        clave = int(input("Ingrese la clave de la materia: "))
        for i in alumnos[n]:
            if i[0] == clave:
                print("Dias: ")
                for j in i[1]:
                    print("- ",j)
                dia = input("Ingrese el dia que desea modificar: ")
                if dia in i[1]:
                    i[1].remove(dia)
                    dia = input("Ingrese el nuevo dia: ")
                    i[1].append(dia)
                    print("Se agrego el dia")
                else:
                    print("No existe ese dia")
    else:
        print("No existe ese numero de cuenta")
    print()

def agregar_alu():
    n = int(input("Ingrese el numero de cuenta a agregar: "))
    if n not in alumnos:
        alumnos[n] = []
        for i in range(3):
            clave = int(input("\nIngrese la clave de la materia que desea agregar: "))
            dias = input("Ingrese los dias de la materia separados por comas: ").split(",")
            alumnos[n].append((clave,dias))
        print("Se agrego el alumno")
    else:
        print("Ya existe ese numero de cuenta")
    print()

def horario():
    n = int(input("Ingrese el numero de cuenta: "))
    if n in alumnos:
        print("Claves de materias y dias: ")
        for i in alumnos[n]:
            print(f"- {i[0]}: ", end="")
            for j in i[1]:
                print(f"{j}, ", end="")
            print()
    else:
        print("No existe ese numero de cuenta")
    print()

def main():
    while True:
        print("\t*** MENU ***")
        print("(1) -- Buscar por numero de cuenta")
        print("(2) -- Eliminar una materia de un alumno")
        print("(3) -- Eliminar un alumno")   
        print("(4) -- Modificar la lista de dias para una materia")
        print("(5) -- Agregar un alumno")
        print("(6) -- Horario de un alumno")
        print("(7) -- Salir")
        opcion = int(input("Ingrese una opcion: "))
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
        elif opcion == 6:
            horario()
        else:
            break

if __name__ == '__main__':
    main()
