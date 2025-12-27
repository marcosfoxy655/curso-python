import random
primeiro=input('qual o nome do primeiro aluno? ')
segundo=input('qual o nome do segundo aluno? ')
terceiro=input('qual o nome do terceiro aluno? ')
quarto=input('qual o nome do quarto aluno? ')
lista=(primeiro, segundo, terceiro, quarto)
escolhido=(random.choice(lista))
print(f'o aluno escolhido foi {escolhido}')