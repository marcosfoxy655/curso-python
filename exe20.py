import random
primeiro=(input('qual o nome do primeiro aluno? '))
segundo=(input('qual o nome do segundo aluno? '))
terceiro=(input('qual o nome do terceiro aluno? '))
quarto=(input('qual o nome do quarto aluno? '))
lista=[primeiro, segundo, terceiro, quarto]
random.shuffle(lista)
print('a ordem da chamada sera')
print(lista)
