from time import sleep
c = int(input('Digite a quantidade de sequência fibonacci: '))
n1 = 0
n2 = 1
n3 = 1
n4 = 0
inicio = 2
print(n1,'→', n2, '→ ', end='')
while inicio < c:
        inicio += 1
        n1 = n2 + n4
        n2 = n2 + n3
        n3 = n1
        print(n1, '→ ' if inicio < c else '', end='')









