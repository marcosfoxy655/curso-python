kilometragem=float(input('quantos kilometros e a viagem? '))
if kilometragem >= 200.0:
    print(f'o valor da viagem e de R${kilometragem*0.45}')
else:
    print(f'o valor da viagem e de R${kilometragem*0.50}')