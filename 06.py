total_mini = 2
cara = float(input('Preço da 1ª miniatura: R$'))
barata = cara
soma = cara
for i in range(total_mini-1):
    print('Preço da ',i+2,'ª miniatura: R$',sep='',end='')
    preco = float(input())
    soma = soma + preco
    if preco > cara:
        cara = preco
    elif preco < barata:
        barata = preco
media = soma /total_mini
print('A miniatura mais cara custou R$',cara,end='')
print(', a mais barata custou R$',barata,end='')
print(' e a média de preços foi de R$',media)