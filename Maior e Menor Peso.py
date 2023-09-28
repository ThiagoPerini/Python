maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite seu peso: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print(f'O maior peso cadastrado: \033[31m{maior}Kgs\033[m\nO menor peso cadastrado: \033[32m{menor}Kgs\033[m')