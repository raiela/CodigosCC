#include <stdlib.h>
#include <stdio.h>
#include <cmath>
#include <iostream>

using namespace std;

int main(){
    int n, d, c, salve = 0;
    long double maior = 0;
    
    cin>>n;
    
    for(int i = 0; i < n; i++){
        cin>>d>>c;
        if(pow(d,c/200.0) > maior){
            maior = pow(d,c/200.0);
            salve = i;
        }
    }
    
    cout<<salve<<endl;

    return 0;
}