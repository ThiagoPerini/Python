valorc = float(input('Qual valor da casa? : '))
salario = float(input('Qual seu salário atualmente? : '))
anosp = float(input('Quantos anos você vai levar para pagar? : '))
prestacao = valorc / (anosp * 12)
limite = (salario * 30) / 100

if prestacao <= limite:
    print(f'Empréstimo aprovado, você pagará mensalmente R${prestacao:.2f} reais')
else:
    print('Empréstimo negado, valor muito alto!')