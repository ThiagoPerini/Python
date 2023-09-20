nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')

print(f'O nome digitado foi: {nome+" "+sobrenome}')
print('A pessoa possui Silva no nome? R: ', 'Silva' in nome+sobrenome)