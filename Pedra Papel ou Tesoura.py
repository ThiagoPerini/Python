import random
jogada = str(input('Pedra, Papel ou Tesoura? : ')).title()
lista = ['Pedra', 'Papel', 'Tesoura']
computador = random.choice(lista)
print(f'Você jogou {jogada} e eu escolhi {computador}')
if jogada == 'Pedra' and computador == 'Tesoura':
    print('Você ganhou!')
elif jogada == 'Papel' and computador == 'Pedra':
    print('Você ganhou!')
elif jogada == 'Tesoura' and computador == 'Papel':
    print('Você ganhou!')
elif jogada == computador:
    print('Empate')
else:
    print('Você perdeu!')
