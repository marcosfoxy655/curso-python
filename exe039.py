from datetime import date
atual=date.today().year
ano=int(input('ano de nascimento: '))
idade= atual - ano
print(f'hoje é {atual} você nasceu em {ano} e voce tem {idade}')
if idade == 18:
    print('Mano, vai logo ir se alistar')
elif idade >18:
    print(f'era pra voce te se alistado a {ano - atual - 18}')
elif idade <18:
    print(f'voce ira se alistar em {ano - atual + 18}')