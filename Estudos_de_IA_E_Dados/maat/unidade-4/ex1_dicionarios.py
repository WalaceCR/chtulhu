lista_pessoas = [['', '']]
quantidade = 5
dicionario = {}

for x in range(quantidade):
    nome = input('Digite seu nome:\n')
    cor_camisa = input('Cor da camisa:\n')
    lista_pessoas.append([nome ,cor_camisa])

lista_ordenada = sorted(lista_pessoas)
for key,value in lista_ordenada:
    dicionario.__setitem__(key, value)

print("After:", dicionario)