# Acosta Porcayo Alan Omar 320206102.

def calc_area(largo, ancho, altura):
    return (largo * altura * 2) + (ancho * altura * 2) + (largo * ancho)

def calc_volumen(largo, ancho, altura):
    return largo * ancho * altura

def costo_total(area, opcion):
    if opcion == 1:
        return area * 70
    elif opcion == 2:
        return area * 120
    elif opcion == 3:
        return area * 180

def main():
    while True:
        largo = float(input("Ingrese el largo del contenedor: "))
        ancho = float(input("Ingrese el ancho del contenedor: "))
        altura = float(input("Ingrese la altura del contenedor: "))
        if (largo >= 1 and largo <= 5) and (ancho >= 1 and ancho <= 5) and (altura >= 1 and altura <= 5):
            break
        print("Error, los valores deben estar entre 1 y 5\n")

    area = calc_area(largo, ancho, altura)
    volumen = calc_volumen(largo, ancho, altura)

    print(f"\nEl area del contenedor es: {area} m2")
    print(f"El volumen del contenedor es: {volumen} m3")

    print("\nEliga el material del contenedor: ")
    print("1. Madera ($70.00 por m2)")
    print("2. Aluminio ($120.00 por m2)")
    print("3. Acero ($180.00 por m2)")
    while True:
        opcion = int(input("Opcion: "))
        if opcion >= 1 and opcion <= 3:
            break
        print("Error, opcion no valida\n")

    costo = costo_total(area, opcion)

    print("\nEl costo total del contenedor es: $", costo)
    if costo >= 3000:
        print("Puede recibir un descuento del 12%\n Nuevo costo: $", costo * 0.88)
        
if __name__ == '__main__':
    main()
