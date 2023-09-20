import random

aluno1 = input('Primeiro nome: ')
aluno2 = input('Segundo nome: ')
aluno3 = input('Terceiro nome: ')
aluno4 = input('Quarto nome: ')

alunos = [aluno1, aluno2, aluno3, aluno4]


print('O aluno sorteado foi : ', random.choice(alunos))
