print('\033[m')
total=0
numero = int(input('digite um numero: '))
for contagem in range(1, numero+1,):
    if numero % contagem == 0:
        print('\033[33m', end='')
        total += 1 
    print(f'{contagem}\033[m', end=' -> ')
print(f'o numero {numero} foi divisivel {total}')
if total == 2:
    print('POR ISSO ELE É PRIMO')
else:
    print('E POR ISSO ELE NÃO E PRIMO')
