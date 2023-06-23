# Acosta Porcayo Alan Omar 320206102.

def main():
    edificios = {
    4: [(30, 12), (31, 21), (32, 17)],
    8: [(33, 15), (34, 24), (35, 20)],
    3: [(36, 16), (37, 22), (38, 19)],
    6: [(39, 25), (40, 16), (41, 21)]
    }

    for e in edificios:
        print(f"Edificio: {e}")
        for s in edificios[e]:
            print(f"Salon: {s[0]} \t Capacidad: {s[1]}")
        print()
        
    while True:
        capacidad = int(input("Ingrese una capacidad: "))
        if capacidad >= 1 and capacidad <= 25:
            break
        print("Cantidad invalida")

    contador = 0
    for e in edificios:
        for s in edificios[e]:
            if s[1] >= capacidad:
                contador += 1
    print(f"Hay {contador} salones con capacidad mayor o igual a {capacidad}")

if __name__ == '__main__':
    main()
