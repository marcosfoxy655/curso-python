sexo = str(input('iforme seu sexo [M/F]: ')).strip().upper() [0]
while sexo not in 'MF':
    sexo = str(input('sexo invalido tente novamente: ')).strip().upper() [0] 
print(f'sexo {sexo} valido')