def conta_pares(v1,v2):
    cont = 0
    if v1 < v2:
        for i in range(v1,v2+1,1):
            if i % 2 == 0:
                cont = cont + 1
    else:
        for i in range(v2,v1+1,1):
            if i % 2 == 0:
                cont = cont + 1
    return cont
valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))
print('A quantidade de valores pares entre os valores fornecidos é',conta_pares(valor1,valor2))