#include <stdio.h>

void bubbleSort(char array[10][10]) {
    char temp[10];

    for(int i = 0; i < 10; i++) {
        for(int j = 0; j < 10 - 1; j++) {
            if(array[j][0] > array[j + 1][0]) {
                for(int k = 0; k < 10; k++) {
                    temp[k] = array[j][k];
                    array[j][k] = array[j + 1][k];
                    array[j + 1][k] = temp[k];
                }
            }
        }
    }
}

int main() {
    char array[10][10];
    FILE *file;

    file = fopen("T10-A-AcostaP-GutierrezG.txt", "r");
    if(file == NULL) {
        printf("Error al abrir el archivo\n");
        return 1;
    }

    for(int i = 0; i < 10; i++)
        fscanf(file, "%s", array[i]);
    fclose(file);

    printf("Array sin ordenar: \n");
    for(int i = 0; i < 10; i ++)
        printf("%d. %s\n",i + 1, array[i]);

    bubbleSort(array);
    printf("\nArray ordenado: \n");
    for(int i = 0; i < 10; i ++)
        printf("%d. %s\n",i + 1, array[i]);

    file = fopen("T10-D-AcostaP-GutierrezG.txt", "w");
    if(file == NULL) {
        printf("Error al abrir el archivo\n");
        return 1;
    }

    printf("\nEl array ordenado se guardo en el archivo T10-D-AcostaP-GutierrezG.txt\n");
    for(int i = 0; i < 10; i ++)
        fprintf(file, "%s\n", array[i]);
    fclose(file);

    return 0;
}