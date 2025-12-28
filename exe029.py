velocidade=float(input('qual a velocidade atual do carro? '))
if velocidade > 80.0:
    multa= (velocidade-80.0)*7.00
    print(f'MULTADO você utrapassou a velocidade maxima de 80\n a multa e de {multa:.2f}')
print('dirija com segurança thau')