media = 0
idadenova = 0
nomevelho = ''
idadevelho = 0
for c in range(1, 5):
    print('-*-' * 25)
    print('-' * 5, f'{c}ª PESSOA', '-' * 5)
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo (M / F): ')).upper()
    media = media + idade
    if c == 1 and sexo in 'M':
        nomevelho = nome
    if sexo == 'M' and idade > idadevelho:
        nomevelho = nome
        idadevelho = idade
    elif sexo == 'F' and idade < 20:
        idadenova = idadenova + 1

print('-*-' * 20)
print(f'O homem mais velho cadastrado foi o {nomevelho} com {idadevelho} anos')
print(f'A media de idade do grupo é de {media / 4} anos')
print(f'A quantidade de mulheres com menos de 20 anos são {idadenova} mulheres')
