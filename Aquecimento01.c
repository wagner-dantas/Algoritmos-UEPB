#include "stdio.h"

int main(void){

    int a,b; 
    char op;
    printf("Digite a operação desejada (+,-,*,/)\n");
    scanf("%c",&op);
    printf("Digite o primeiro valor:\n");
    scanf("%d",&a);
    printf("Digite o segundo valor: \n");
    scanf("%d",&b);
    
    switch(op){
    case '+': printf("a soma é %d \n",a+b);
    break;
    case '-': printf("a subtração é %d \n",a-b);
    break;
    case '*': printf("a multiplicação é %d \n",a*b);
    break;
    case '/': printf("a divisão é %d \n",a/b);
    break;
    }  
    return 0;
}