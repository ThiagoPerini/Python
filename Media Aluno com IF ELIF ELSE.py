nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'A media foi {media}')
if media < 5:
    print('O aluno está REPROVADO')
elif media >= 5 and media <= 7:
    print('O aluno está de RECUPERAÇÃO')
else:
    print('O aluno está APROVADO')