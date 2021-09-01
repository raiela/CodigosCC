#include <iostream>
 
using namespace std;
 
int main() {
 
    /**
     * Escreva a sua solução aqui
     * Code your solution here
     * Escriba su solución aquí
     */
    int pa, pb, t, cont;
    double ga, gb;

    scanf("%d", &t);
    for(int i = 0; i < t; i++){
        scanf("%d %d %lf %lf", &pa, &pb, &ga, &gb);
        cont = 0;
        while(pa <= pb){
            pa = pa + (pa*(ga/100));
            pb = pb + (pb*(gb/100));
            cont++;
            if(cont > 100){
                printf("Mais de 1 seculo.\n");
                break;
            }
        }
        if(cont <= 100) printf("%d anos.\n", cont);
    }
 
    return 0;
}