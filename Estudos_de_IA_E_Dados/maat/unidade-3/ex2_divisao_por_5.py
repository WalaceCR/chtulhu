lista_numeros = [[0, 0]]
dicionario_numeros = {}

for x in range(1000, 1999):
    if (x%11==5):
        lista_numeros.append([x ,x])

for key,value in lista_numeros:
    dicionario_numeros.__setitem__(key, value)

print("After:", dicionario_numeros)
print("After:", lista_numeros)



