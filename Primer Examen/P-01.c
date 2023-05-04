//Acosta Porcayo Alan Omar 320206102
#include <stdio.h>

int main() {
    //Problema 1
    int matriz[6][3] = {{3,5,7},{4,3,6},{4,7,2},{8,10,1},{9,2,10},{1,3,5}};
    int contador1 = 0, contador2 = 0;

    printf("Datos de la Matriz:\n");
    for (int i = 0; i < 6; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", matriz[i][j]);
        }
        printf("\n");
    }

    for (int i = 0; i < 6; i ++) {
        if(matriz[i][1] <= 3) contador1++;
    }
    printf("\nCantidad de programas que utilizan f2 3 veces o menos: %d\n", contador1);

    for (int i = 0; i < 6; i ++) contador2 += matriz[i][0];
    printf("Cantidad de usos de la funcion 1: %d\n", contador2);

    //Problema 2
    int array[10] = {9,10,4,7,4,2,7,3,8,6}, *ap, suma = 0;
    ap = &array[0];
    
    printf("\n\nDatos del Array:\n");
    for(int i = 0; i < 10; i ++) printf("%d ", *(ap + i));
    for(int i = 0; i < 10; i ++) suma += *(ap + i);
    printf("\n\nPromedio de los datos del array; %d\n", suma / 10);

    return 0;
}