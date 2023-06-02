import numpy as np

def desglose(cantidad, billetes):
    if cantidad == 0:
        return []
    else:
        if cantidad >= billetes[0]:
            return [billetes[0]] + desglose(cantidad - billetes[0], billetes)
        else:
            return desglose(cantidad, billetes[1:])
        
def insertion_sort(a):
    for i in range(1, 10):
        j = i
        while j > 0 and a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1
    return a

def main():
    billetes = np.array([500, 200, 100, 50, 20, 10, 5, 2, 1])
    cantidad = int(input('Ingrese la cantidad de dinero: '))
    print(f'El desglose de {cantidad} es: {desglose(cantidad, billetes)}')

    strings = np.array(['Santiago', 'Mateo', 'Sebastian', 'Leonardo', 'Matias', 'Emiliano', 'Diego', 'Daniel', 'Miguel', 'Alexander'])
    print('\nEl array de strings es:')
    print(strings)
    print('El array ordenado por inserción es:')
    print(insertion_sort(strings))

if __name__ == '__main__':
    main()
