
sair = False
primeiro_numero=float(input('primeiro numero: '))
segundo_numero=float(input('segundo numero: '))
while not sair:
    print('''oque você deseja
[1] somar
[2] multiplicar
[3] o maior
[4] outros numeros
[5] sair''')
    opção = int(input('qual opção você quer: '))
    if opção == 1:
        soma = primeiro_numero + segundo_numero
        print(f'a soma de {primeiro_numero} + {segundo_numero} = {soma}')
    elif opção == 2:
        produto = primeiro_numero * segundo_numero
        print(f'o produto de {primeiro_numero} x {segundo_numero} = {produto}')
    elif opção == 3:
        if primeiro_numero > segundo_numero:
            maior = primeiro_numero
        elif primeiro_numero < segundo_numero:
            maior = segundo_numero
        print(f'entre o {primeiro_numero} e o {segundo_numero} o maior e o {maior}')
    elif opção == 4:
        primeiro_numero=float(input('primeiro numero: '))
        segundo_numero=float(input('segundo numero: '))

    elif opção == 5:
        sair = True

    else:
        a
print('adeus volte sempre')