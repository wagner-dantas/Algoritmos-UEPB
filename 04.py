def IMC(p,h):
    return p / (h**2)
peso = float(input('Informe o peso: '))
altura = float(input('Informe a altura: '))
imc = IMC(peso,altura)
print('IMC:',imc)
if imc < 18.5:
    print('Baixo peso.')
elif imc < 24.9:
    print('Peso normal.')
elif imc < 29.9:
    print('Sobrepeso')
else:
    print('Obesidade.')