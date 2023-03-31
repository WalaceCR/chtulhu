import math


numero_solicitado = int(input('Digite um valor: \n'))
##AQUI COLOCAR O FATORIAL
dicionario = {
  "valor_digitado_de_" + str(numero_solicitado): numero_solicitado,
  "fatorial_de_" + str(math.factorial(numero_solicitado)): math.factorial(numero_solicitado)
}

print('Dicionário antes\n===============\n',dicionario)
'''
for x in range(4):
    numero_solicitado = int(input('Digite um valor: \n'))
    dicionario.__setitem__("valor_digitado", numero_solicitado)
    dicionario.__setitem__("fatorial", math.factorial(numero_solicitado))

print('Dicionário depois\n===============\n',dicionario)
print('Apenas valor digitado\n============\n',dicionario['valor_digitado'])
print('Apenas fatorial\n============\n',dicionario['fatorial'])

for x in range(4):
    numero_solicitado = int(input('Digite um valor: \n'))
    dicionario.update({"valor_digitado": numero_solicitado, "fatorial": math.factorial(numero_solicitado)})

print('Dicionário depois do update\n===============\n',dicionario)
print('Apenas valor digitado\n============\n',dicionario['valor_digitado'])
print('Apenas fatorial\n============\n',dicionario['fatorial'])

'''

lista_numeros = [[0, 0]]
dicionario_numeros = {}

for x in range(4):
    numero_solicitado = int(input('Digite um valor: \n'))
    lista_numeros.append([numero_solicitado,  math.factorial(numero_solicitado)])

for chave,valor in lista_numeros:
    dicionario_numeros.__setitem__(chave,valor)
    dicionario.update({"valor_digitado_de_" + str(chave): chave, "fatorial_de_" + str(valor): valor})

print('Dicionário simples\n===============\n',dicionario_numeros)
print('Dicionário depois\n===============\n',dicionario)