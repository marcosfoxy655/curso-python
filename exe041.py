idade=int(input('qual sua idade? '))
if idade <= 9:
    print('você e um atleta mirim')
elif idade <= 14 and idade >= 10:
    print('você e um atleta infatil')
elif idade <= 19 and idade >= 15:
    print('você e um atleta junior')
elif idade <= 25 and idade >= 20:
    print('você e um atleta senior')
else:
    print('você e um atleta master')