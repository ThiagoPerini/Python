frase = input('Digite uma frase: ')
final = int(len(frase))

print('A letra (a) apareceu :', frase.count('a'), 'vezes')
print('A letra (a) aparece pela primeira vez na posição:',frase.find('a'))
print('A letra (a) aparece pela ultima vez na posição:',frase.rfind('a'))
