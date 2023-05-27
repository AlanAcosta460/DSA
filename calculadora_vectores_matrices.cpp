#include <bits/stdc++.h>
#define MAX_VEC 50
#define MAX_MAT 5
using std::cin; using std::cout;

double vec1[MAX_VEC], vec2[MAX_VEC], vec3[MAX_VEC], vecAux[MAX_VEC], sum = 0, escalar;
double mat1[MAX_MAT][MAX_MAT], mat2[MAX_MAT][MAX_MAT], matAux[MAX_MAT][MAX_MAT];
int tam, rows, cols;

int pedirOpcion(int opMax) {
    std::string op;
    int opInt;
    do {
        cout<<"> ";
        cin>>op;
        opInt = stoi(op);
        if (opInt < 1 or opInt > opMax) cout<<"Opcion Invalida\n";
    } while(opInt < 1 or opInt > opMax);
    return opInt;
}

int menuPrincipal() {
    system("cls");
    cout<<"********** Menu Principal **********\n";
    cout<<".: Vectores :.\n";
    cout<<"1)  Suma\n2)  Resta\n3)  Vector por escalar\n4)  Producto escalar\n5)  Producto vectorial\n6)  Producto mixto\n\n";
    cout<<".: Matrices :.\n";
    cout<<"7)  Suma\n8)  Resta\n9)  Matriz por escalar\n10) Producto\n11) Traza\n12) Transpuesta\n13) Inversa\n14) Salir\n\n";
    cout<<".: Seleccione una opcion :.\n";
    return pedirOpcion(14);
}

int menuRetorno() {
    cout<<"\n\n********** Menu de Retorno **********\n";
    cout<<"1) Repetir operacion\n2) Volver al menu principal\n3) Salir\n\n";
    cout<<".: Seleccione una opcion :.\n";
    return pedirOpcion(3);
}

void fillVec(int n, bool dim) {
    if(dim) {
        cout<<".: Ingrese el tamanio de los vectores :.\n";
        tam = pedirOpcion(MAX_VEC);
    }
    cout<<"\n.: Vector 1 :.\n";
    for(int i = 0; i < tam; i ++) cin>>vec1[i];
    if(n == 1) return;
    cout<<".: Vector 2 :.\n";
    for(int i = 0; i < tam; i ++) cin>>vec2[i];
    if(n == 2) return;
    cout<<".: Vector 3 :.\n";
    for(int i = 0; i < tam; i ++) cin>>vec3[i];
}

void showVec(double vec[MAX_VEC]) {
    cout<<"\n.: Resultado :.\n";
    for(int i = 0; i < tam; i ++) cout<<vec[i]<<"\t";
    cout<<'\n';
}

void fillMat(int n, bool dim) {
    if(dim) {
        cout<<".: Ingrese el numero de filas :.\n";
        rows = pedirOpcion(MAX_MAT);
        cout<<".: Ingrese el numero de columnas :.\n";
        cols = pedirOpcion(MAX_MAT);
    }
    cout<<"\n.: Matriz 1 :.\n";
    for(int i = 0; i < rows; i ++) for(int j = 0; j < cols; j ++) cin>>mat1[i][j];
    if(n == 1) return;
    cout<<".: Matriz 2 :.\n";
    for(int i = 0; i < rows; i ++) for(int j = 0; j < cols; j ++) cin>>mat2[i][j];
}

void showMat(double mat[][MAX_MAT]) {
    cout<<"\n.: Resultado :.\n";
    for(int i = 0; i < rows; i ++) {
        for(int j = 0; j < cols; j ++) cout<<mat[i][j]<<"\t";
        cout<<"\n";
    }
}

void sumaVec() {
    cout<<"***** Suma de Vectores *****\n";
    fillVec(2, true);
    for(int i = 0; i < tam; i ++) vec1[i] += vec2[i];
    showVec(vec1);    
}

void restaVec() {
    cout<<"***** Resta de Vectores *****\n";
    fillVec(2, true);
    cout<<"\n1) Vector 1 - Vector 2\n2) Vector 2 - Vector 1\n\n";
    cout<<".: Selecciones una opcion :.\n";
    if(pedirOpcion(2) == 1) {
        for(int i = 0; i < tam; i ++) vec1[i] -= vec2[i];
        showVec(vec1);
    } else {
        for(int i = 0; i < tam; i ++) vec2[i] -= vec1[i];
        showVec(vec2);   
    }
}

void vecPorEscalar() {
    cout<<"***** Vector por Escalar *****\n";
    fillVec(1, true);
    cout<<"\n.: Escalar :.\n> ";
    cin>>escalar;
    for(int i = 0; i < tam; i ++) vec1[i] *= escalar;
    showVec(vec1);
}

void productoEscalar() {
    cout<<"***** Producto Escalar *****\n";
    fillVec(2, true);
    sum = 0;
    for(int i = 0; i < tam; i ++) sum += vec1[i] + vec2[i];
    cout<<"\n.: Resultado :.\n"<<sum;
}

void productoVectorial() {
    cout<<"***** Producto Vectorial *****\n";
    tam = 3;
    fillVec(2, false);
    vecAux[0] = (vec1[1] * vec2[2]) - (vec1[2] * vec2[1]); 
    vecAux[1] = (- 1) * ((vec1[0] * vec2[2]) - (vec1[2] * vec2[0]));
    vecAux[2] = (vec1[0] * vec2[1]) - (vec1[1] * vec2[0]);
    showVec(vecAux);
}

void productoMixto() {
    cout<<"***** Producto Mixto *****\n";
    tam = 3;
    fillVec(3, false);
    vecAux[0] = (vec2[1] * vec3[2]) - (vec2[2] * vec3[1]);
    vecAux[1] = (- 1) * ((vec2[0] * vec3[2]) - (vec2[2] * vec3[0]));
    vecAux[2] = (vec2[0] * vec3[1]) - (vec2[1] * vec3[0]);
    sum = 0;
    for(int i = 0; i < 3; i ++) sum += vec1[i] * vecAux[i];
    cout<<"\n.: Resultado :.\n"<<sum;
}

void sumaMat() {
    cout<<"***** Suma de Matrices *****\n";
    fillMat(2, true);
    for(int i = 0; i < rows; i ++) for(int j = 0; j < cols; j ++) mat1[i][j] += mat2[i][j];
    showMat(mat1);
}

void restaMat() {
    cout<<"***** Resta de Matrices *****\n";
    fillMat(2, true);
    cout<<"\n1) Matriz 1 - Matriz 2\n2) Matriz 2 - Matriz 1\n\n";
    cout<<".: Selecciones una opcion :.\n";
    if(pedirOpcion(2) == 1) {
        for(int i = 0; i < rows; i ++) for(int j = 0; j < cols; j ++) mat1[i][j] -= mat2[i][j];
        showMat(mat1);
    } else {
        for(int i = 0; i < rows; i ++) for(int j = 0; j < cols; j ++) mat2[i][j] -= mat1[i][j];
        showMat(mat2);  
    }
}

void matPorEscalar() {
    cout<<"***** Matriz por Escalar *****\n";
    fillMat(1, true);
    cout<<"\n.: Escalar :.\n> ";
    cin>>escalar;
    for(int i = 0; i < rows; i ++) for(int j = 0; j < cols; j ++) mat1[i][j] *= escalar;
    showMat(mat1);
}

void productoMat() {
    int cols2, rows2;
    cout<<"***** Producto de Matrices *****\n";
    do {
        cout<<".: Ingrese el numero de filas de la Matriz 1 :.\n";
        rows = pedirOpcion(MAX_MAT);
        cout<<".: Ingrese el numero de columnas de la Matriz 1 :.\n";
        cols = pedirOpcion(MAX_MAT);
        cout<<".: Ingrese el numero de filas de la Matriz 2 :.\n";
        rows2 = pedirOpcion(MAX_MAT);
        cout<<".: Ingrese el numero de columnas de la Matriz 2 :.\n";
        cols2 = pedirOpcion(MAX_MAT);
        if (cols != rows2) 
            printf("\nEl numero de columnas de la Matriz 1 debe ser igual al numero de filas de la Matriz 2\n");
        printf("\n");
    } while(cols != rows2);
    cout<<"\n.: Matriz 1 :.\n";
    for(int i = 0; i < rows; i ++) for(int j = 0; j < cols; j ++) cin>>mat1[i][j];
    cout<<".: Matriz 2 :.\n";
    for(int i = 0; i < rows2; i ++) for(int j = 0; j < cols2; j ++) cin>>mat2[i][j];
    for(int i = 0; i < rows; i ++) {
        for(int j = 0; j < cols2; j ++) {
            matAux[i][j] = 0;
            for(int k = 0; k < cols; k ++) matAux[i][j] += mat1[i][k] * mat2[k][j];
        }
    }
    cols = cols2;
    showMat(matAux);
}

void traza() {
    cout<<"***** Traza de una Matriz *****\n";
    cout<<".: Ingrese el numero de filas y columnas de la matriz cuadrada :.\n";
    rows = pedirOpcion(MAX_MAT);
    cols = rows;
    fillMat(1, false);
    sum = 0;
    for(int i = 0; i < rows; i ++) {
        for(int j = 0; j < cols; j ++) {
            if(i == j) sum += mat1[i][j];
        }
    }
    cout<<"\n.: Resultado :.\n"<<sum;
}

void transpuesta() {
    cout<<"***** Transpuesta de una Matriz *****\n";
    fillMat(1, true);
    cout<<"\n.: Resultado :.\n";
    for(int i = 0; i < cols; i ++) {
        for(int j = 0; j < rows; j ++) cout<<mat1[j][i]<<"\t";
        cout<<"\n";
    }
}

void inversa() {
    cout<<"***** Inversa de una Matriz 2x2 *****\n";
    rows = 2; 
    cols = 2;
    fillMat(1, false);
    sum = (mat1[0][0] * mat1[1][1]) - (mat1[0][1] * mat1[1][0]); 
    if (sum == 0) printf("\nLa matriz no tiene inversa\n");
    else {
        matAux[0][0] = mat1[1][1] / sum;
        matAux[0][1] = -mat1[0][1] / sum;
        matAux[1][0] = -mat1[1][0] / sum;
        matAux[1][1] = mat1[0][0] / sum;
        showMat(matAux);
    }
}

int main() {
    int op;
    cout<<std::fixed<<std::setprecision(2);
    inicio: op = menuPrincipal();
    seleccion: system("cls");
    switch (op) {
        case 1: sumaVec(); break;
        case 2: restaVec();break;
        case 3: vecPorEscalar(); break;
        case 4: productoEscalar(); break;
        case 5: productoVectorial(); break;
        case 6: productoMixto(); break;
        case 7: sumaMat(); break;
        case 8: restaMat(); break;
        case 9: matPorEscalar(); break;
        case 10: productoMat(); break;
        case 11: traza(); break;
        case 12: transpuesta(); break;
        case 13: inversa(); break;
        default: goto fin; break;
    }
    switch (menuRetorno()) {
        case 1: goto seleccion; break;
        case 2: goto inicio; break;
    }
    fin: 
    cout<<"\nGracias por usar el programa\n\n"; 
    system("pause"); 
    return 0;
}
