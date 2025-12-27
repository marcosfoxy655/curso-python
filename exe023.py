numero=int(input('digite um numero entre 1 e 9999: '))
unidade= numero // 1 % 10
dezena= numero // 10 % 10
centena= numero // 100 % 10
milhar= numero // 1000 % 10
print(f'analizando o numero {numero}')
print(f'a unidade e {unidade}')
print(f'a dezena e {dezena}')
print(f'a centena e {centena}')
print(f'a milhar e {milhar}')