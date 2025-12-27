palavra = str(input('escreva uma palavra: ')).upper().strip()

print(f'a letra A aparece {palavra.count('A')} de vezes')
print(f'a primeira letra A apareceu na posição {palavra.find('A')+1}')
print(f'a ultima letra A apareceu na posição {palavra.rfind('A')+1}')