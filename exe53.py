frase=str(input('digite uma frase: ')).strip().upper()
palavras=frase.split()
junto=''.join(palavras)
invertido=''
for lentra in range(len(junto) - 1, -1, -1):
    invertido += junto[lentra]
print(invertido)
if junto == invertido:
    print('temos PALINDROMO')
else:
    print('essa frase NÃO e um PALINDROMO')