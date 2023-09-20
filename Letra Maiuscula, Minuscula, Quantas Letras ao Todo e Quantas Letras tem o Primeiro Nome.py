nomec = input('Digite seu nome completo: ')
sobrenome = input('Digite seu sobrenome: ')

#Nome com todas as letras maiúsculas
print('Nome digitado com todas as letras maiúsculas: ')
print(nomec.upper())
#Nome com todas as letras minúsculas
print('Nome digitado com todas as letras minúsculas: ')
print(nomec.lower())
#Quantas letras ao todo, sem contar os espaços
print('Quantas letras ao todo sem contas os espaços: ')
print(len(nomec+sobrenome)-nomec.count(" "))
#Quantas letras o primeiro nome possui
print('Quantas letras o primeiro nome possui: ')
print(len(nomec))