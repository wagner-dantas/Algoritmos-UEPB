#def divisivel (v1,v2):
#    if v1 % v2 == 0:
#        return True
#    else:
#        return False
def divisivel(v1,v2):
    return v1 % v2 == 0
valor1 = int(input('Valor 1: '))
valor2 = int(input('Valor 2: '))
if divisivel(valor1,valor2):
    print(valor1,'é divisivel por',valor2)
else:
    print(valor1,'não é divisivel por',valor2)