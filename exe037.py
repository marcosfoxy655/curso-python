numero=int(input('digite um numero: '))
print('''[1] BINARIO
[2] OCTAL
[3] HEXADECIMAL''')
opção=int(input('qual sua opção: '))
if opção == 1:
    print(f'o numero {numero} em BINARIO fica {bin(numero)}')
elif opção == 2:
    print(f'o numero {numero} em OCTAL fica {oct(numero)}')
elif opção == 3:
    print(f'o numero {numero} em HEXADECIMAL fica {hex(numero)}')
else:
    print('\033[31mseu codigo esta ivalido, tente novamente\033[m')