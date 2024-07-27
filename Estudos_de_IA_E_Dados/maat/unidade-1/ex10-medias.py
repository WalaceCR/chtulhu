lista_notas = []

for x in range(4):
    notas = int(input('Digite sua nota esse mês\n'))
    lista_notas.append(notas)

media = 0
soma = 0
for nota in lista_notas:
    soma += nota

media = soma / len(lista_notas)

print(f'Suas notas foram: \n{lista_notas[0]}\n{lista_notas[1]}\n{lista_notas[2]}\n{lista_notas[3]}\nSua média é {media}')
