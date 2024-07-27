import csv

arquivo = 'dados_entrada.csv'
arquivo_aberto_csv = open(arquivo)
##abro o arquivo

print(type(arquivo_aberto_csv))
##vejo o tipo do arquivo

csvreader = csv.reader(arquivo_aberto_csv)

header = []
header = next(csvreader)
print('Cabeçalho', header)
##VEJO APENAS OS CABEÇALHOS


rows = []
for row in csvreader:
    rows.append(row)
##ADICINONO LINHAS DO CSV NUMA LISTA

for linha in rows:
    print(linha)
##PRINTO AS PARADAS DA LISTA GERADA

print('======================//======================\nLENDO COM WITH\n======================//======================')


with open(arquivo, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print('Cabeçalho', header)
print('Linha', rows)


print('======================//======================\nLENDO COM WITH E READLINES\n======================//======================')

with open(arquivo) as file:
    content = file.readlines()
header = content[:1]
rows = content[1:]
print('Cabeçalho', header)
print('Linha', rows)

arquivo_aberto_csv.close()


