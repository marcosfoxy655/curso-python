from datetime import date
maior_de_idade=0
jovem=0
atual=date.today().year
for contagem in range(1, 8):
    nascimento=int(input(f'qual a data de nascimeto da {contagem}° pessoa: '))
    idade=atual-nascimento
    if idade >= 21:
        maior_de_idade += 1
    else:
        jovem += 1
print(f'''ao todo tivemos {maior_de_idade} pessoas maiores de idade
e tambem temos {jovem} pessoas jovems''')