import math
cateto_oposto=float(input('qual o cateto oposto? '))
cateto_adjacente=float(input('qual o cateto adjacente? '))
hipotenusa= math.hypot(cateto_oposto, cateto_adjacente)
print(f'se o cateto opsto for {cateto_oposto} e o cateto adjacente for {cateto_adjacente} a hipotenusa {hipotenusa:.2f}')