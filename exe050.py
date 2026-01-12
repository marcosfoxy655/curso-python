soma = 0
contagem = 0
for vez in range(1, 7):
    numero=int(input(f'digite o {vez}° numero:'))
    if numero % 2 == 0:
        soma += vez
        contagem += 1
print(f'você imformou {contagem} pares numeros e a soma deles é igual a {soma}')