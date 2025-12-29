from datetime import date
ano=int(input('qual o ano que vc quer ser quiser analisar o ano atual digite 0: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano%100 != 0 or ano%400 ==0:         
        print(f'o ano de {ano} é BISSEXTO')
else:
        print(f'o ano de {ano} não é BISSEXTO')