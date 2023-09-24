from random import randint
from time import sleep
print('-+-'*20)
print('Tente adivinhar o número que estou pensando')
print('-+-'*20)
numero = int(input('Digite um número entre 0 e 5 : '))
nums = randint(0,5)
print('Processando...')
sleep(2)
print(f'Eu pensei em {nums} e você digitou {numero}')
if numero == nums:
    print('Parabéns você ganhou!')
else:
    print('Você perdeu, tente novamente!')