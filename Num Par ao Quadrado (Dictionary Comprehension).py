dicio = {'a':1, 'b':2, 'c': 3, 'd': 4}
quadrado = {c: vlr**2 for c, vlr in dicio.items() if not(vlr%2)}
print(quadrado)