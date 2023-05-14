import numpy as np
import matplotlib 
import matplotlib.pyplot as plt

# Variables Globales
marcas = ['Ford  ', 'BMW   ', 'Toyota', 'Tesla ', 'Nissan']
meses = ['Oct', 'Nov', 'Dic']
porcentaje_marca, porcentaje_mes = np.zeros([5,3]), np.zeros([5,3])

def show_mat(mat):
    rows_tot = mat.sum(axis = 1)
    cols_tot = mat.sum(axis = 0)

    for i in range(0, 3):
        print(f'\t{meses[i]}', end='')
    print('\tTotal')
    
    for i in range(0, 5):
        print(marcas[i], end='\t')
        for j in range(0, 3):
            print(mat[i][j], end='\t')
        print(rows_tot[i])
    
    print('Total', end='\t')
    for i in range(0, 3):
        print(cols_tot[i], end='\t')
    print()

def contribucion_marca(mat):
    cols_tot = mat.sum(axis = 0)

    for i in range(0, 5):
        for j in range(0, 3):
            porcentaje_marca[i][j] = round((mat[i][j] / cols_tot[j]) * 100, 2)

def contribucion_mes(mat):
    rows_tot = mat.sum(axis = 1)

    for i in range(0, 5):
        for j in range(0, 3):
            porcentaje_mes[i][j] = round((mat[i][j] / rows_tot[i]) * 100, 2)

def grafica(mat): #TODO Mostrar la grafica de la matriz porcentaje_marca
    # x =
    # y =
    # plt.plot(x, y)
    font1 = {'family':'serif','color':'green','size':20}
    plt.title("Porcentaje de contribución (por marca)", fontdict = font1, loc='center')
    plt.grid()
    plt.show()

def guardar_en_archivo(mat):
    rows_tot = mat.sum(axis = 1)
    cols_tot = mat.sum(axis = 0)

    with open('T9-AcostaP-GutierrezG.txt', 'w') as f:
        f.write('\t')
        for i in range(0, 3):
            f.write(f'\t{meses[i]}')
        f.write('\tTotal\n')

        for i in range(0, 5):
            f.write(f'{marcas[i]}\t')
            for j in range(0, 3):
                f.write(f'{mat[i][j]}\t')
            f.write(str(rows_tot[i]))
            f.write('\n')
        
        f.write('Total \t')
        for i in range(0, 3):
            f.write(f'{str(cols_tot[i])}\t')


def main():
    matriz = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 0, 1], [2, 3, 4]])
    
    print('********** Ventas Totales **********')
    show_mat(matriz)
    
    print('\n******* % de contribución (por marca) *******')
    contribucion_marca(matriz)
    show_mat(porcentaje_marca)

    print('\n******* % de contribución (por mes) *******')
    contribucion_mes(matriz)
    show_mat(porcentaje_mes)

    print('\n***** Venta mas baja *****')
    print(f'Marca: {marcas[np.argmin(matriz) // 3]}\tMes: {meses[(np.argmin(matriz)) % 3]}')

    print('\n***** Venta mas alta *****')
    print(f'Marca: {marcas[np.argmax(matriz) // 3]}\tMes: {meses[(np.argmax(matriz)) % 3]}')

    guardar_en_archivo(matriz)
    print('\n*** Se guardo la matriz original en un archivo ***')

    
if __name__ == '__main__':
    main()
