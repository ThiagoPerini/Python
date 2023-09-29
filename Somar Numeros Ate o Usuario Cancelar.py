cont = 0
c = soma = 0
while c != 999:
    c = int(input('Digite um numero inteiro: '))
    if c != 999:
        cont += 1
        soma = soma + c
print(f'Foram digitados {cont} numeros e a soma entre eles foi {soma}')