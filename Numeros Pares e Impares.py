soma = 0
contpar = 0
contimpar = 0
for c in range(1, 7):
    numero = int(input('Digite um numero inteiro: '))
    if numero % 2 == 0:
        soma = soma + numero
        contpar = contpar + 1
    else:
        contimpar = contimpar + 1
print(f'Você informou {contpar+contimpar} numeros, sendo eles, {contpar} pares e {contimpar} impares\n e a soma dos numeros pares informados foram:  {soma}')