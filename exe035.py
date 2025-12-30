print("=="*20)
print('analisador de triangulos')
print("=="*20)

primeira_reta=float(input('qual o comprimento da primeira reta? '))
segunda_reta=float(input('qual o comprimento da segunda reta? '))
terceira_reta=float(input('qual o comprimento da terceira reta? '))
if primeira_reta < segunda_reta + terceira_reta and segunda_reta < primeira_reta + terceira_reta and terceira_reta < primeira_reta + segunda_reta:
    print(f'as retas podem SIM se torna um TRIANGULO')
else:
    print(f'as retas NÃO podem se torna um TRIANGULO')