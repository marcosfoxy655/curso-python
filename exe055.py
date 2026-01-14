maior =0
menor = 0
for pessoas in range(1, 6):
    peso=float(input(f'qual o peso da {pessoas}° pessoa? (kg) '))
    if pessoas == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'''o maior peso lido é {maior}Kg
o menor peso lido é {menor}Kg''')