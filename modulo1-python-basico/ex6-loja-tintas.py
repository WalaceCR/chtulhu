print('======================//======================\nA cobertura de 1 litro de tinta é de 3 metros quadrados\nA tinta é vendida em latas de 18 litros\nSeu custo da lata é de R$ 80,00\n')
#input de dados
metros_quadrados = float(input('Área a ser pintada em metros quadrados\n'))

#demais variáveis
cobertura_tinta_metros_quadrados = 3# cobertura de 1 litro de tinta para cada 3 metros quadrados de área
lata_tinta = 18#lata vem com 18 litros
custo_lata = 80.00#custo da lata

#calculo
#para vender uma lata de tinta o usuário deve informar no mínimo 54 metros
#1 lata de tinta pinta 54 metros na cobertura padrão
litros_tinta = metros_quadrados / cobertura_tinta_metros_quadrados
latas_de_tinta_recomendadas = litros_tinta / lata_tinta

preco_total = latas_de_tinta_recomendadas * custo_lata

#apresentação
print(f'======================//======================\nO recomendado é que você compre {int(latas_de_tinta_recomendadas)} latas de tinta\n======================//======================\nSeu gasto será R$ {preco_total:.2f}')