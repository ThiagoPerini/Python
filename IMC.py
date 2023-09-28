peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
if altura.is_integer():
    altura = altura / 100
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Seu imc é de {imc:.2f} seu estado é : Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print(f'Seu imc é de {imc:.2f} seu estado é : Peso ideal')
elif imc >= 25 and imc < 30:
    print(f'Seu imc é de {imc:.2f} seu estado é : Sobrepeso')
elif imc >= 30 and imc <= 40:
    print(f'Seu imc é de {imc:.2f} seu estado é : Obesidade')
else:
    print(f'Seu imc é de {imc:.2f} seu estado é : Obesidade Mórbida')




