from datetime import date
anoatual = date.today().year
menor = 0
maior = 0
for c in range(1, 8):
    anonasc = int(input('Digite seu ano de nascimento: '))
    soma = anoatual - anonasc
    if soma < 18:
        menor += + 1
    else:
        maior += + 1
print(f'Menores de idade: {menor}\nMaiores de idade: {maior}')