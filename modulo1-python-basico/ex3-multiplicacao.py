quanto_voce_ganha_por_hora = input('Quanto voce ganha por hora ?\n')
quantas_horas_voce_trabalhou = input('Quanto voce trabalhou?\n')

multiplicacao = int(quantas_horas_voce_trabalhou) * float(quanto_voce_ganha_por_hora)

print('Você ganhou esse mês ', str(multiplicacao))