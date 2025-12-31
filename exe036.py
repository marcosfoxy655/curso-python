casa=float(input('qual o valor da casa? R$'))
salario=float(input('qual o salario da pessoa? R$'))
anos=int(input('quantos anos irá pagar? '))
prestações = casa / (anos * 12)
minimo= salario / 100 * 30
print(f'para pagar uma casa de R${casa} com salario de R${salario} em {anos} anos as prestações são de {prestações} com o minimo de {minimo}')
if prestações < minimo:
    print('emprestimo CONCEDIDO')
else:
    print('emprestimo NEGADO')


#mundo 2