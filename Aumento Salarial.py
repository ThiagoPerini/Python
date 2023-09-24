salario = float(input('Qual é o valor do seu salário: '))
aumento = salario + (salario * 15) / 100

print(f'Com o aumento de 15% seu salario passou de R${salario:.2f} para R${aumento:.2f}')