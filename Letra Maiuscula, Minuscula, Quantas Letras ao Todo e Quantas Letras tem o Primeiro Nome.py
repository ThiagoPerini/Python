nomec = input('Digite seu nome completo: ')
dividido = nomec.split()

#Nome com todas as letras maiúsculas
print('Nome digitado com todas as letras maiúsculas: ')
print(nomec.upper())
#Nome com todas as letras minúsculas
print('Nome digitado com todas as letras minúsculas: ')
print(nomec.lower())
#Quantas letras ao todo, sem contar os espaços
print('Quantas letras ao todo sem contar os espaços: ')
print(len(nomec)-nomec.count(" "))
#Quantas letras o primeiro nome possui
print('Quantas letras o primeiro nome possui: ')
print(len(dividido[0]))
