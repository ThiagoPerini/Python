from datetime import date
anonsc = int(input('Informe seu ano de nascimento: '))
sexo = int(input('Qual seu gênero? [1] Masculino [2] Feminino: '))
anoatual = date.today().year
idade = anoatual - anonsc

if sexo == 2:
    print('Você não precisa se alistar')
elif idade < 18:
    alistamento = 18 - idade
    print(f'Ainda faltam {18 - idade} anos para você se alistar')
    print(f'Seu alistamento será em {alistamento + anoatual}')
elif idade == 18:
    print('Está na hora de você se alistar!')
elif idade > 18:
    alistamento = idade - 18
    print(f'Já passou {idade - 18} anos do tempo do alistamento')
    print(f'Seu alistamento foi em {anoatual - alistamento}')
