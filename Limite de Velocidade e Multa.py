velocidade = int(input('Digite a velocidade que você passou: '))

if velocidade > 80:
    print('Você foi multado!')
    multa = (velocidade - 80) * 7
    print(f'O valor da multa será \033[31mR${multa:.2f}\033[m reais')
else:
    print('Sem Multas,Boa Viagem!')