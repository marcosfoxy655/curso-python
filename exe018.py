import math
angulo=float(input('digite um angulo: '))
seno=math.sin(math.radians(angulo))
cosseno=math.cos(math.radians(angulo))
tangente=math.tan(math.radians(angulo))
print(f'o SENO de {angulo}é {seno:.3f}\n o COSEENO de {angulo} é {cosseno:.3f}\n a TANGENTE de {angulo} é {tangente:.3f}')