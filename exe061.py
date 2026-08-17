print("gerador PA")
print("-" * 10)
primeiro_termo = int(input('primeiro termo: '))
razão = int(input("razão: "))
termo = primeiro_termo
cont = 1
while cont <= 10:
    print(f'{termo} ->', end=' ')
    termo += razão
    cont += 1
print('fim')