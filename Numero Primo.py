numero = int(input('Digite um numero inteiro: '))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        tot = tot + 1
if tot == 2:
    print('Numero primo')
else:
    print('Não é numero primo')
