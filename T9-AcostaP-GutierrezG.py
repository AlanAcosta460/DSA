def pedir_dato():
    dato = -1
    while dato < 0:
        dato = int(input("-> "))
    return dato

def leer_punto(i):
    print(f"Ingrese el valor de x{i}: ")
    x = pedir_dato()
    print(f"Ingrese el valor de y{i}: ")
    y = pedir_dato()
    print()
    punto = (x, y)
    return punto

def calcular_distancia(tupla):
    return ((tupla[1][0] - tupla[0][0]) ** 2 + (tupla[1][1] - tupla[0][1]) ** 2) ** 0.5

def calcular_pendiente(tupla):
    return (tupla[1][1] - tupla[0][1]) / (tupla[1][0] - tupla[0][0])

def calcular_perimetro(tupla):
    return calcular_distancia((tupla[0], tupla[1])) + calcular_distancia((tupla[1], tupla[2])) + calcular_distancia((tupla[0], tupla[2]))

def actividad_1():
    tupla_1 = (leer_punto(1), leer_punto(2))
    
    print(f"La distancia entre los puntos es: {calcular_distancia(tupla_1)}")
    
    pendiente = calcular_pendiente(tupla_1)
    print(f"La pendiente de la recta es: {pendiente}")
    if pendiente == 0:
        print("La pendiente es horizontal")
    elif tupla_1[0][0] == tupla_1[1][0]:
        print("La pendiente es vertical")
    else:
        print("La pendiente es inclnada")
    print()
    
    tupla_2 = (tupla_1[0], tupla_1[1], leer_punto(3))

    print(f"El perimetro del triangulo es: {calcular_perimetro(tupla_2)}")

    lista = [tupla_2[0], tupla_2[1], tupla_2[2]]
    print(f"Lista de puntos: {lista}")


def actividad_2():
    print("Ingrese un número entero positivo: ")
    dato_string = str(pedir_dato())

    numeros = {"0":"cero", "1":"uno", "2":"dos", "3":"tres", "4":"cuatro", "5":"cinco", "6":"seis", "7":"siete", "8":"ocho", "9":"nueve"}
    print("El número en palabras es: ", end=" ")
    for i in range(0, len(dato_string)):
        for j in range(0, 10):
            if dato_string[i] == str(j):
                print(numeros[str(j)], end=" - ")
    print()
    
def main():
    print("********************** Tarea 9 **********************")
    while True:
        print("\n1) Actividad 1\n2) Actividad 2\n3) Salir")
        opcion = pedir_dato()
        print()
        if opcion == 1:
            actividad_1()
        elif opcion == 2: 
            actividad_2()
        else:
            break

if __name__ == "__main__":
    main()