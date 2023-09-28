numero = int(input('Digite um número inteiro qualquer: '))
tipo = int(input('Qual será a base de conversão? (1 = Binario, 2 = Octal, 3 = Hexadecimal) : '))

if tipo == 1:
    convertido = bin(numero)[2:]
    print(f'O valor {numero} convertido para binário é : {convertido}')
elif tipo == 2:
    convertido = oct(numero)[2:]
    print(f'O valor {numero} convertido para octal é : {convertido}')
elif tipo == 3:
    convertido = hex(numero)[2:]
    print(f'O valor {numero} convertido para hexadecimal é : {convertido}')
else:
    print('O tipo informado é inválido!')
