numero = int(input('digite um numero par descobrir seu fatorial: '))
mostrando = numero
fatorial = 1
print(f'calculano {numero}! = {numero} ', end=' ')
while mostrando > 1:
    print(f'x {mostrando - 1} ', end=' ')
    fatorial *= mostrando
    mostrando -= 1
print(f'= {fatorial}')