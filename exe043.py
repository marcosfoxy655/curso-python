peso = float(input(' quals eu peso? (Kg) '))
altura = float(input('qual sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'sua altura é {altura}, seu peso é {peso}, e seu imc é {imc:.1f}')
if imc <= 18.5:
    print('você esta ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('você esta com o PESO IDEAL')
elif 25 <= imc < 40:
    print('você esta com SOBREPESO')
elif 30 <= imc < 40:
    print('você esta OBESO')
else:
    print('você esta com OBESIDADE MORBIDA')
    