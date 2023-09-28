c1 = float(input('Primeiro lado: '))
c2 = float(input('Segundo lado: '))
c3 = float(input('Terceiro lado: '))
medidas = [c1, c2, c3]
if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('Pode formar um triangulo', end=" ")
    if c1 == c2 and c1 == c3:
        print('EQUILATERO')
    elif c1 == c2 or c1 == c3:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('Os segmentos não podem formar um triângulo')