n = int(input('Qual a quantidade de pessoas? '))
soma = 0
for i in range(n):
    idade = int(input('Idade: '))
    soma = soma + idade
media = soma / n
print('Média de idades:',media)
if media > 0 and media <= 60:
    print('Turma jovem.')
elif media > 25 and media <= 60:
    print('Turma adulta.')
elif media > 60:
    print('Turma idosa.')
else:
    print('Média de idades inválida.')