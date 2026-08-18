print('sequencia de fibonacci')
print('-' * 24)
termos = int(input('quantos termos? '))
cont = 0
termo1 = 0
termo2 = 1
termo3 = 1
while cont < termos:
    if cont == 0:
        print(f'{termo1} ->', end=' ')
        cont += 1
    else:
        while cont < termos:
            print(f'{termo3} ->', end=' ')
            termo3 = termo1 + termo2
            termo1 = termo2
            termo2 = termo3
            cont += 1
print('FIM')