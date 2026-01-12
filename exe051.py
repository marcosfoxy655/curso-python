print(':='*25)
print('{:^50}'.format('PROGRESSÃO ARITIMETICA'))
print(':='*25)
primeiro_termo=int(input('PRIMEIRO_TERMO: '))
razão=int(input('RAZÃO: '))
decimo= primeiro_termo + (10 - 1)* razão
for contagem in range(primeiro_termo, decimo+1, razão):
    print(f'{contagem} -> ', end='')
print('ACABOU')