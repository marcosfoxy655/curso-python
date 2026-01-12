print('{:=^50}'.format(' LOJAS RAPOSAS '))
preço=float(input('qual o preço da compra: '))
print(''' FORMAS DE PAGAMENTO
[1] avista dinheiro/cheque
[2] avista cartão
[3] ate 2x no cartão sem juros
[4] 3x ou mais no cartão com juros
''')
opção=int(input('qual das formas de pagamento você? '))
if opção == 1:
    preço_final=preço - (preço / 100 * 10)
    print(f'você pagou {preço_final}')
elif opção == 2:
    preço_final=preço - (preço / 100 * 5)
    print(f'você pagou {preço_final}')
elif opção == 3:
    print(f'você pagou {preço_final}')
elif opção == 4:
    preço_final=preço + (preço / 100 * 20)
    parcelas=int(input('quantas parcelas'))
    print(f'você parcelou em {parcelas}x')
    print(f'você pagou {preço_final}')
else:
    print('ERRO digite un dos numeros acima')