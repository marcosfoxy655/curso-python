from random import randint
print('==='*15)
print('estou pensando em um numero entre 0 e 10')
print('==='*15)
print('')
computador = randint(0,10)
acertou = False
erro = 0
numero=int(input('qual numero você acha que eu estou pensando? '))
if numero != computador:
    erro += 1
while not acertou:
    if numero < computador:
        numero = int(input('mais tente novamente: '))
        erro += 1
    elif numero > computador:
        numero = int(input('menos tente novamentes: '))
        erro += 1
    elif numero == computador:
        acertou = True
print(f'parabens você acertou. com {erro} tentativas')