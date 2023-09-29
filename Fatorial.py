numero = int(input('Digite um numero: '))
f = 1
c = numero
print(f'O fatorial de {numero} é ', end='')
while c > 0:
   print(c, 'x ' if c > 1 else '= ', end='')
   f *= c
   c -= 1
print(f)

