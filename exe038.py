primeiro_numero=int(input('qual o primeiro numero? '))
segundo_numero=int(input('qual o segundo numero? '))
if primeiro_numero > segundo_numero:
    print('o \033[1mPRIMEIRO\033[m numero e o maior')
elif segundo_numero > primeiro_numero:
    print('o \033[1mSEGUNDO\033[m numero e o maior')
elif primeiro_numero == segundo_numero:
    print('os dois numeros são \033[1mIGUAIS\033[m')