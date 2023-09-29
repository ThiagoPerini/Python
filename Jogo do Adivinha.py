from random import randint

numero = int(input('Digite um numero: '))
palpites = 1
computador = randint(0,10)
while numero != computador:
    palpites += 1
    if numero > computador:
        print('Menos...', end='')
    else:
        print('Mais...', end='')
    numero = int(input('Tente novamente: '))
print('-=-'* 16)
print(f'Eu pensei em {computador} e você digitou {numero}')
print(f'Você fez {palpites} palpites e acertou o numero {numero}')
print('-=-'* 16)