lista = []
media_idade = 0
media_peso = 0
contador = 0
while True:
    try:
        sobrenome = input('Digite seu sobrenome: ')
        if sobrenome == '':
             break
        idade = int(input('Digite sua idade: '))
        altura = int(input('Digite sua altura em centímetros: '))
        peso = float(input('Digite seu peso em KG: '))
        pessoa = [sobrenome, idade, altura, peso]
        lista.append(pessoa)
        media_idade += idade
        media_peso += peso
        contador += 1
    except (ValueError, NameError) as erro:
        print(f'Ocorreu um erro: {erro}')
        continue
nova_lista = sorted(lista)
for valores in nova_lista:
    print(f'Sobrenome: {valores[0]}, Idade: {valores[1]}, Altura: {valores[2]}, Peso: {valores[3]}')
print(f'Media das idades: {media_idade/ contador}')
print(f'Media dos pesos: {media_peso / contador}')

