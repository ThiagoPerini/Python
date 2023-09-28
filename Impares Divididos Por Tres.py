soma = 0
cont = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 == 1:
        cont = cont + 1
        soma = soma + c
        print(c)
print(f'A soma de {cont} valores é {soma}')