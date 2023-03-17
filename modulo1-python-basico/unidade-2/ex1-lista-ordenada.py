
quantidade_desejada = int(input('Quantidade de itens na lista para ordenar\n'))

lista_numeros = []

for x in range(quantidade_desejada):
    valores = int(input('Digite um valor:\n'))
    lista_numeros.append(valores)

print('Lista não ordenada\n==============//==============')
for a in lista_numeros:
    print(a)

lista_ordenada = sorted(lista_numeros)
print('Lista ordenada\n==============//==============')
for b in lista_ordenada:
    print(b)


