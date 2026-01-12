from random import randint
from time import sleep
jogada = ('x')
itens=['pedra', 'papel', 'tesoura']
computador = randint(0, 2)
jogador=int(input('''[0] pedra
[1] papel
[2] tesoura
qual opção você escolhe: '''))
print(' JO')
sleep(1.55)
print('KEN')
sleep(1.5)
print('PÔ!!!')
sleep(1)

print('-=-='*11)
print(f'o computador escolheu {itens[computador]}')
if jogador == 0:
    print('o jogador escolheu pedra')
    jogada=0
elif jogador == 1:
    print('o jogador escolheu papel')
    jogada=1
elif jogador == 2:
    print('o jogador escolheu tesoura')
    jogada=2
else:
    print('BOOM o computador explodiu')
    print('você ganhou ROUBANDO')
if computador == 0 and jogada == 2 or computador == 1 and jogada == 0 or computador == 2 and jogada == 1:
    print('o computador GANHOU')
elif jogada == 0 and computador == 2 or jogada == 1 and computador == 0 or jogada == 2 and computador == 1:
    print('o jogador GANHOU')
elif computador == jogada:
    print('EMPATE')
print('-=-='*11)