viagem = float(input('Digite a distância da sua viagem: '))

if viagem <= 200:
    valor = viagem * 0.50
else:
    valor = viagem * 0.45
print(f'O valor da sua viagem custará R${valor:.2f} reais')