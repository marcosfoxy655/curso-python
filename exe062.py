print("gerador PA")
print("-" * 10)
primeiro_termo = int(input('primeiro termo: '))
razão = int(input("razão: "))
termo = primeiro_termo
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} ->', end=' ')
        termo += razão
        cont += 1
    print('pausa')
    mais = int(input('quantos termos a mais você quer?'))
print('FIM')