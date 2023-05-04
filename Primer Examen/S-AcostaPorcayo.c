#include <stdio.h>
#include <string.h>

typedef struct Programa {
    int idProg;
    char descProg[100]; 
} Programa;

void mostrarContenido(Programa array[10], int tamanio) {
    for(int i = 0; i < tamanio; i ++) printf("%d\t%s\n", array[i].idProg, array[i].descProg);
}

int main() {
    Programa listaProg[4] = {{11, "Captura"}, {13, "Bajas"}, {16, "Reporte"}, {18, "Consulta"}};

    printf("Array Original: \n");
    mostrarContenido(listaProg, 4);

    strcpy(listaProg[2].descProg, "ReporteNew");
    printf("\nArray Modificado: \n");
    mostrarContenido(listaProg, 4);
}