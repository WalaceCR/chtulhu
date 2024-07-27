from numpy import genfromtxt
import csv
import numpy as np

arquivo = 'dados_entrada.csv'
meus_dados = genfromtxt('dados_entrada.csv', delimiter=',',dtype=None,encoding='utf8')
##delimiter é a string separadora
##dtype, sem ele volta tudo nan
##encoding é encoding mesmo

print(str(meus_dados))
##NÃO FUNFA
##print(meus_dados['endereco'])

with open(arquivo) as f:
    reader = csv.reader(f)
    columns = next(reader)
    colmap = dict(zip(columns, range(len(columns))))

csv_convertido_em_matriz = np.matrix(np.loadtxt(arquivo, delimiter=",", skiprows=1,dtype=np.str_,encoding='utf8'))
print(csv_convertido_em_matriz[:, colmap['idade']])
##coluna especifica

for idade in csv_convertido_em_matriz[:, colmap['idade']]:
    print('idade no array: ', str(idade))

print(str(csv_convertido_em_matriz))
##todas as colunas sem o cabeçalho