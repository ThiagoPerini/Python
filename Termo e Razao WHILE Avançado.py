termo = int(input('Digite o primeiro termo: '))
razao = int(input('Razao: '))
soma = termo
termototal = 0
resposta = 1
vari = 10
while termototal < vari:
    print(soma, '→ ', end='')
    termototal = termototal + 1
    soma += razao
    while termototal == vari and resposta != 0:
        print('PAUSA')
        resposta = int(input('Quantos termos você quer mostrar a mais? : '))
        termototal = 0
        vari = resposta
        while termototal < vari:
            print(soma, '→ ', end='')
            termototal += 1
            soma += razao
print('Programa finalizado...')
