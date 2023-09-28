precop = float(input('Valor do produto: '))
print('Métodos de Pagamento\n[1]Dinheiro\n[2]Cheque\n[3]Cartão\n[4]2x no Cartão\n[5]3x ou Mais no Cartão')
metodo = int(input('Digite o método do pagamento: '))

if metodo == 1 or metodo == 2:
    desconto = precop - (precop * 10) / 100
    print(f'Desconto de 10% no pagamento àvista com dinheiro/cheque, o valor final ficará R${desconto:.2f}')
elif metodo == 3:
    desconto = precop - (precop * 5 ) / 100
    print(f'Desconto de 5% no pagamento àvista com cartão, o valor final ficará R${desconto:.2f}')
elif metodo == 4:
    print('No pagamento em 2x no cartão o valor permanece igual')
elif metodo == 5:
    valor = precop + (precop * 20) / 100
    print(f'No pagamento em 3x ou mais no cartão o valor recebe um juros de 20% e passa de R${precop:.2f} para R${valor:.2f}')
else:
    print('Opção inválida de pagamento, tente novamente!')