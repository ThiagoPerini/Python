numero = input('Digite um numero entre 0 a 9999: ')
numero = numero[:4]
print('Unidade:', numero[3:])
print('Dezena:', numero[2:3])
print('Centena :', numero[1:2])
print('Milhar:', numero[0:1])