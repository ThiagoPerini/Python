resposta = ''
media = 0
cont = 0
while resposta != 'N':
    numero = int(input('Digite um numero inteiro: '))
    resposta = str(input('Quer adicionar outro valor?[S/N] : ')).upper()
    media = media + numero
    cont += 1
    if cont == 1:
        menor = numero
        maior = numero
    else:
        if numero < maior:
         menor = numero
        if numero > maior:
         maior = numero
print('-' * 40)
print(f'A media dos valores digitados foi {media / cont}')
print(f'Maior numero digitado {maior}\nMenor numero digitado {menor}')