num1 = int(input('Primeiro número inteiro: '))
num2 = int(input('Segundo número inteiro: '))

if num1 > num2:
    print(f'O primeiro valor é maior')
elif num2 > num1:
    print(f'O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')
