import numpy as np

quantidade_desejada = int(input('Quantidade de itens na lista para ordenar\n'))

lista_numeros = []

for x in range(quantidade_desejada):
    valores = int(input('Digite um valor:\n'))
    lista_numeros.append(valores)

lista_ordenada = sorted(lista_numeros)

novo_array = np.array(lista_ordenada)

print(novo_array)