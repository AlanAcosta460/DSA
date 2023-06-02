import random

def binario(x):
    if x == 0:
        return 0
    else:
        return x % 2 + 10 * binario(x // 2)
    
def contar_elementos(a, lim_inf, lim_sup):
    if(a==[]):
        return 0
    if a[0] >= lim_inf and a[0] <= lim_sup:
        return 1 + contar_elementos(a[1:], lim_inf, lim_sup)
    else:
        return contar_elementos(a[1:], lim_inf, lim_sup)

def main():
    x = int(input('Ingrese un numero entero: '))
    x_bin = binario(x)
    print(f'El numero {x} en binario es: {x_bin}')

    array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 10):
        array[i] = random.randint(10, 25)
    
    while True:
        lim_inf = int(input('\nIngrese el limite inferior: '))
        lim_sup = int(input('Ingrese el limite superior: '))
        if lim_inf < lim_sup and lim_inf >= 10 and lim_inf <= 25 and lim_sup >= 10 and lim_sup <= 25:
            break
    
    print(f'\nEl array es: {array}')
    print(f'La cantidad de elementos entre {lim_inf} y {lim_sup} es: {contar_elementos(array, lim_inf, lim_sup)}')

if __name__ == '__main__':
    main()
