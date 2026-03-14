somaidade = 0
mediaidade = 0
maioridadehomem = 0
mulhermenor20 = 0
maioridadenome = ''
for pessoas in range(1,5):
    print(f'----{pessoas}°----')
    nome = str(input(f'nome: ')).strip()
    idade = int(input(f'idade '))
    sexo = str(input(f'sexo [M][F]')).strip()
    somaidade += idade
    if pessoas == 1 and sexo in 'Mm':
        maioridadehomem = idade
        maioridadenome = nome
    if sexo in 'mM' and idade > maioridadehomem:
        maioridadehomem = idade
        maioridadenome = nome
    if sexo in 'fF' and idade <= 20:
        mulhermenor20 += 1
    

mediaidade = somaidade / 4
print(f'a media de idade do grupo é {mediaidade}')
print(f'o homem mais velho é {maioridadenome} e a idade dele é {maioridadehomem}')
print(f'tem {mulhermenor20} mulheres menores que 20 anos')