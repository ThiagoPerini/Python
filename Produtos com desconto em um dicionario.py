lista_produtos = {
    'geladeira': 2500,
    'microondas': 350,
    'fogão': 1300,
    'liquidificador': 220
}
nova_lista = {produto: valor - ((valor * 5) / 100) for produto, valor in lista_produtos.items()}
print(f'Lista: {lista_produtos}')
print(f'Lista com desconto de 5% : {nova_lista}')
