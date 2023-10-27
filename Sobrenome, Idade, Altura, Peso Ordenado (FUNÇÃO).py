def sobre_info(valor):
    while True:
        valor = input('Digite um sobrenome: ')
        if valor.isalpha():
            break
        elif valor == '':
            break
        else:
            print('Digite um valor válido!')
    return valor


def id_info(valor):
    while True:
        valor = input('Digite sua idade: ')
        if valor.isalnum():
            break
        else:
            print('Digite um valor válido!')
    return int(valor)


def altura_info(valor):
    while True:
        valor = input('Digite sua altura em CM: ')
        if valor.isalnum():
            break
        else:
            print('Digite um valor válido!')
    return valor


def peso_info(valor):
    while True:
        valor = input('Digite seu peso arredondado: ')
        if valor.isalnum():
            break
        else:
            print('Digite um valor valido!')
    return int(valor)


sobrenome = ''
lista = []
peso = 0
altura = 0
idade = 0
media_idade = 0
media_peso = 0
cont = 0
while True:
    sobrenome = sobre_info(sobrenome)
    if sobrenome == '':
        break
    idade = id_info(idade)
    altura = altura_info(altura)
    peso = peso_info(peso)
    pessoa = [sobrenome, idade, altura, peso]
    lista.append(pessoa)
    media_idade += idade
    media_peso += peso
    cont += 1
lista_ordenada = sorted(lista)
for itens in lista_ordenada:
        print(f'Nome: {itens[0]}, Idade: {itens[1]}, Altura: {itens[2]}, Peso: {itens[3]}')
if cont > 0:
    print(f'A media das idades é: {media_idade/cont }')
    print(f'A media dos pesos é: {media_peso/cont}')
