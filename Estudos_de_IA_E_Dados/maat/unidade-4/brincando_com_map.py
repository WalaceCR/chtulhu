def ordena_lista(lista):
    return sorted(lista)

lista_geral = ['Zebra', 'Banana', 'Abc', 'XPYO']

print('CHAMANDO FUNÇÃO', ordena_lista(lista_geral))

##COM A FUNÇÃO ORDENA_LISTA MONTADA
variavel_map = list(map(ordena_lista, lista_geral))
print('COM APENAS LIST', variavel_map)

##COM LAMBDA
variavel_map = list(map(lambda lista_ordenada: sorted(lista_ordenada), lista_geral))
print('COM LIST E MAP', variavel_map)