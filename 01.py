def reajustar_salario(salario,percentual):
    return salario + salario * percentual / 100
num_funcionarios = 10
for i in range (num_funcionarios):
    nome = input('Nome do Funcionario: ')
    cargo = input('Cargo: ')
    salario = float(input('Salario: '))
    if cargo == 'Supervisor':
        novo_salario = reajustar_salario(salario,10)
    elif cargo == 'Operário':
        novo_salario = reajustar_salario(salario,7)
    print('O novo salário do funcionario',nome,'é de R$',novo_salario)