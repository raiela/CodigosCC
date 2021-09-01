#include <iostream>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int main(){
    long long int n, ind = 0, valor, lista[1002000], soma = 0, estrela = 0, roubo = 0;

    scanf("%lld", &n);
    for (int i = 0; i < n; i++){
        scanf("%lld", &valor);
        soma += valor;
        lista[i] = valor;
    }
    

    while (lista[ind] != 0){
        
        if(ind >= estrela)
                estrela = ind;
            
        if(lista[ind] % 2 != 0){
            if(ind == n-1){
                roubo += 1;
                break;
            }
        }
        if(lista[ind] % 2 == 0){
            if(ind == 0){
                roubo += 1;
                break;
            }
        }
            
        int save = lista[ind];
        
        if(lista[ind] != 0){
            roubo += 1;
            lista[ind] -= 1;
            if((save % 2 != 0) && (ind != n-1))
                ind ++;
            else if((save % 2 == 0) && (ind > 0))
                ind --;
        }
        
    }
    
    printf("%lld %lld\n", estrela+1, soma-roubo);

    return 0;
}