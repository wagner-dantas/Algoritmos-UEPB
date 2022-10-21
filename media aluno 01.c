/*Etruturas de Decisão*/
#include <stdio.h>
//if, else / switch ...  case
int main(void){
  
    float n1,n2,media;
    printf("Digite a nota 1 e a nota 2:\n ");
    scanf("%f %f",&n1,&n2);
    
    media = (n1+n2)/2;
    
    if (media>=7){
        printf("Aprovado!\n");
    }
    else if(media<6 && (media>=3)){
        printf("Final!\n");
    }
    else{
        printf("Reprovado!\n");
    }
    printf("Media: %.2f",media);

    return 0;
}


