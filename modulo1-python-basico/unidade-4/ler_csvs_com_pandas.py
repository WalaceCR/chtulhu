import pandas as pd

arquivo = 'dados_entrada.csv'

data= pd.read_csv(arquivo)
print(data)
#todo o dataframe

print(data['endereco'])
#apenas a coluna

print('Todas as colunas', data.columns)

print('Endereço', data.endereco)

