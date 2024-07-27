valor_desejado = int(input('Digite um valor: \n'))
descricao_valor = ''

if valor_desejado % 2 == 0:
    valor_desejado = valor_desejado + 5
    descricao_valor = 'par'
else:
    valor_desejado = valor_desejado + 8
    descricao_valor = 'ímpar'

print(f'Seu valor é {valor_desejado} e ele é {descricao_valor}')

