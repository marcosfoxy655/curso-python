number = 0
final = 0
cont = 0
while number != 999:
    number = int(input('escolha um numero [ESCOLHA 999 PARA PARAR]: '))
    final += number
    cont += 1
print (f'quantidade foi de {cont - 1} o valor final foi {final - 999}')