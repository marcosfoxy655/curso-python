salario=float(input('qual o salario do funcionario? R$'))
if salario <= 1250.00:
    salario_atual = (salario / 100 * 15)+ salario
else:
    salario_atual = (salario / 100 * 15)+ salario
print(f'o salario que antes era R${salario} agora passa a ser R${salario_atual}')