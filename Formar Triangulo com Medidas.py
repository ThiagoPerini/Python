c1 = int(input('Digite um comprimento: '))
c2 = int(input('Digite o segundo comprimento: '))
c3 = int(input('Digite o terceiro comprimento: '))

if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('Pode formar um triangulo')
else:
    print('Não pode formar um triângulo')