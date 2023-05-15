import numpy as np
import matplotlib 
import matplotlib.pyplot as plt

# Variables Globales
marcas = ['Ford  ', 'BMW   ', 'Toyota', 'Tesla ', 'Nissan']
meses = ['Oct', 'Nov', 'Dic']

def show_mat(mat): # Imprime la matriz con formato
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

def main():
    matriz = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 0, 1], [2, 3, 4]])
    rows_tot = matriz.sum(axis = 1) # Total de cada fila
    cols_tot = matriz.sum(axis = 0) # Total de cada columna
    porcentaje_marca, porcentaje_mes = np.zeros([5,3]), np.zeros([5,3])
    
    # Matriz original
    print('********** Ventas Totales **********')
    show_mat(matriz) 
    
    # Matriz con el porcentaje de contribución de cada marca al total del mes
    print('\n******* % de contribución (por marca) *******')
    for i in range(0, 5):
        for j in range(0, 3):
            porcentaje_marca[i][j] = round((matriz[i][j] / cols_tot[j]) * 100, 2)
    show_mat(porcentaje_marca)

    # Matriz con el porcentaje de contribución de cada mes al total de la marca
    print('\n******* % de contribución (por mes) *******')
    for i in range(0, 5):
        for j in range(0, 3):
            porcentaje_mes[i][j] = round((matriz[i][j] / rows_tot[i]) * 100, 2)
    show_mat(porcentaje_mes)

    # Venta mas baja
    print('\n***** Venta mas baja *****')
    print(f'Marca: {marcas[np.argmin(matriz) // 3]}\tMes: {meses[(np.argmin(matriz)) % 3]}')

    # Venta mas alta
    print('\n***** Venta mas alta *****')
    print(f'Marca: {marcas[np.argmax(matriz) // 3]}\tMes: {meses[(np.argmax(matriz)) % 3]}')

    # Gráfico de linea con los datos de la matriz porcentaje_marca
    # TODO Mostrar la grafica de la matriz porcentaje_marca
    # x =
    # y =
    # plt.plot(x, y)
    # font1 = {'family':'serif','color':'green','size':20}
    # plt.title("Porcentaje de contribución (por marca)", fontdict = font1, loc='center')
    # plt.grid()
    # plt.show()

    # Datos de la matriz original guardados en un archivo
    print('\n*** Se guardo la matriz original en un archivo ***')
    with open('T9-AcostaP-GutierrezG.txt', 'w') as f:
        f.write('\t')
        for i in range(0, 3):
            f.write(f'\t{meses[i]}')
        f.write('\tTotal\n')

        for i in range(0, 5):
            f.write(f'{marcas[i]}\t')
            for j in range(0, 3):
                f.write(f'{matriz[i][j]}\t')
            f.write(str(rows_tot[i]))
            f.write('\n')
        
        f.write('Total \t')
        for i in range(0, 3):
            f.write(f'{str(cols_tot[i])}\t')
        
    
if __name__ == '__main__':
    main()
