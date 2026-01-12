numero=float(input('digite um numero: '))
print('-='*12)
for contagem in range(0, 11,):
    print(f'{numero} x {contagem:2} = {contagem*numero}')
print('-='*12)