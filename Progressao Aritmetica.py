ptermo = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))
print(f'Primeiro termo: {ptermo}, Razao: {razao}')
print('Os 10 primeiros termos são: ')
for c in range (1, 11):
    print(f'{ptermo} → ', end="")
    ptermo = ptermo + razao
print('FIM')