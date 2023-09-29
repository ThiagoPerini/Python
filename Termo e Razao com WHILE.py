termo = int(input('Digite o primeiro termo: '))
razao = int(input('Razao: '))
soma = termo
termototal = 0
while termototal < 10:
    print(soma,'→ ', end='')
    termototal = termototal + 1
    soma += razao
print('Fim')