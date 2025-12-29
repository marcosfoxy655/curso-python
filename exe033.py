primeiro_numero=int(input('qual o primeiro numero? '))
segundo_numero=int(input('qual o segundo numero? '))
terceiro_numero=int(input('qual o terceiro numero? '))
menor=primeiro_numero
if segundo_numero<primeiro_numero and segundo_numero<terceiro_numero:
    menor=segundo_numero
if terceiro_numero<primeiro_numero and terceiro_numero<segundo_numero:
    menor=terceiro_numero
maior=primeiro_numero
if segundo_numero>primeiro_numero and segundo_numero>terceiro_numero:
    maior=segundo_numero
if terceiro_numero>primeiro_numero and terceiro_numero>segundo_numero:
    maior=terceiro_numero
print(f'o menor numero è {menor}')
print(f'o maior numero è {maior}')