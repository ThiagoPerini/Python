frase = input('Digite uma frase: ').strip().upper()
frase = frase.replace('á' ,'A').replace('â','A').replace('Á','A').replace('Â','A')
print('A letra A apareceu :', frase.count('A'), 'vezes')
print('A letra A aparece pela primeira vez na posição:',frase.find('A')+1)
print('A letra A aparece pela ultima vez na posição:',frase.rfind('A')+1)