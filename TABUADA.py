numero = int(input('Qual tabuada você quer ver: '))
print(f'Tabuada do {numero}')
for c in range(1, 11):
    print(f'{numero} x {c} = {numero * c}')
