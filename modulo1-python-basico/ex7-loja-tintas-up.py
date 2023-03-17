import math

# pede ao usuário o tamanho da área a ser pintada em metros quadrados
area = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))

# calcula a quantidade de litros de tinta necessária
litros = area / 6

# calcula a quantidade de latas de 18 litros e galões de 3,6 litros necessários
latas = math.ceil(litros / 18)
galoes = math.ceil(litros / 3.6)

# calcula o preço para comprar apenas latas de 18 litros
preco_latas = latas * 80

# calcula o preço para comprar apenas galões de 3,6 litros
preco_galoes = galoes * 25

# mistura latas e galões para minimizar o desperdício de tinta
latas_mix = int(litros / 18)
resto = litros % 18
if resto != 0:
    galoes_mix = math.ceil(resto / 3.6)
else:
    galoes_mix = 0
preco_mix = latas_mix * 80 + galoes_mix * 25

# adiciona 10% de folga
litros += litros * 0.1

# exibe os resultados
print(f"Quantidade de tinta a ser comprada: {litros:.2f} litros")
print(f"Preço ao comprar apenas latas de 18 litros: R$ {preco_latas:.2f}")
print(f"Preço ao comprar apenas galões de 3,6 litros: R$ {preco_galoes:.2f}")
print(f"Preço ao misturar latas e galões: R$ {preco_mix:.2f}")