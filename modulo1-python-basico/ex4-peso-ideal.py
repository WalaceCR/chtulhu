qual_sua_altura = input('Qual sua altura ?\n')
qual_genero = input('Qual seu gênero biológico ?\n')

peso_ideal = 0.00

if str(qual_genero).upper() == "M":
    peso_ideal = (72.7 * float(qual_sua_altura)) - 58
elif str(qual_genero).upper() == "F":
    peso_ideal = (62.1 * float(qual_sua_altura)) - 44.7
else:
    print('Digite um valor válido no campo gênero')
    
print('Peso ideal é ', str(peso_ideal))