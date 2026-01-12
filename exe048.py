soma = 0
contagem_segundaria = 0
for contagem_primaria in range(1, 501, 2):
    if contagem_primaria % 3 == 0:
        soma = soma + contagem_primaria
        contagem_segundaria = contagem_segundaria + 1
print(f'a soma dos {contagem_segundaria} solitados e igual a {soma}')
