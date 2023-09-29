# Digitar dois valores para atribuir as variáveis val1 e val2
val1 = float(input('Primeiro valor: '))
val2 = float(input('Segundo valor: '))
# Inicializando variáveis necessárias
resposta = 0
soma = 0
menor = maior = 0
# Estrutura de repetição (Enquanto a resposta for diferente de 5)
while resposta != 5:
    resposta = int(input("O que você deseja fazer? \n"
                         "[1] Somar\n"
                         "[2] Multiplicar\n"
                         "[3] Maior\n"
                         "[4] Novos Números\n"
                         "[5] Sair do Programa\n"))
    # Condições: 
    # Resposta = 1 (Somar)
    if resposta == 1:
        soma = val1 + val2
        print(f'A soma dos dois valores é {soma:.0f}')
    # Resposta = 2 (Multiplicar)
    elif resposta == 2:
        soma = val1 * val2
        print(f'A multiplicação dos dois valores é {soma:.0f}')
    # Resposta = 3 (Mostrar maior e menor)
    elif resposta == 3:
        if val1 > val2:
            maior = val1
            menor = val2
        else:
            maior = val2
            menor = val1
        print(f'O maior valor é o {maior:.0f} e o menor é o {menor:.0f}')
    # Resposta = 4 (Perguntar novos números)
    elif resposta == 4:
        val1 = float(input('Primeiro valor: '))
        val2 = float(input('Segundo valor: '))
    elif resposta == 5:
        print('Finalizando....')
    else:
        print('Opção Inválida, tente novamente : ')

