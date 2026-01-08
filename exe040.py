nota1=float(input('qual primeira nota desse aluno? '))
nota2=float(input('qual segunda nota desse aluno? '))
media=(nota1 + nota2)/2
if media >= 7:
    print(f'media {media} APROVADO')
elif media >= 5 and media <= 6.9:
    print(f'media {media} RECUPEÇÃO')
else:
     print(f'media {media} REPROVADO')
