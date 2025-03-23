#include <stdio.h>

int main() {
    int numero;
    
    printf("Digite um numero: ");
    scanf("%d", &numero);
    
    if (numero % 2 == 0) {
        printf("O numero %d e par.\n", numero);
    } else {
        printf("O numero %d é impar.\n", numero);
        printf("O numero %d é impar.\n", numero);
    }
    
    return 0;
}