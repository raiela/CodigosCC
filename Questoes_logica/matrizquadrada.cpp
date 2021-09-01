#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<cstdio>

using namespace std;

int main(){
    int matriz[120][120];
    int n, dia = 0, auxDig, meio, valor, quandreOne;
    
    while(scanf("%d", &n) != EOF){
        auxDig = n-1;
        meio = n/2;
        quandreOne = n/3;
        
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                matriz[i][j] = 0;
                if(j == i)
                    matriz[i][j] = 2;
                if(j == auxDig)
                    matriz[i][j] = 3;
                if(j >= quandreOne && i >= quandreOne && j < n-quandreOne && i < n-quandreOne)
                    matriz[i][j] = 1;
                if(j == meio && i == meio)
                    matriz[i][j] = 4;
            }
            auxDig--;
        }

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                printf("%d", matriz[i][j]);
            }
            printf("\n");
        }
        printf("\n");
    }       
        
        return 0;
}