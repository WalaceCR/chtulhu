quanto_voce_ganha_por_hora = input('Quanto voce ganha por hora ?\n')
quantas_horas_voce_trabalhou = input('Quanto voce trabalhou neste mês?\n')

salario_bruto = int(quantas_horas_voce_trabalhou) * float(quanto_voce_ganha_por_hora)

ir = (float(salario_bruto) * 11) / 100
inss = (float(salario_bruto) * 8) / 100
sindicato = (float(salario_bruto) * 5) / 100
total_descontos = ir + inss + sindicato
salario_liquido = float(salario_bruto) - float(total_descontos)

print('==========================//==========================\nSalário bruto do mês: ', str(salario_bruto) + ' R$', '\n',
    'INSS do mês: ', str(inss) + ' R$', '\n'
    'Imposto de Renda do mês: ', str(ir) + ' R$', '\n'
    'Valor ao Sindicato do mês: ', str(sindicato) + ' R$', '\n'
    'Salário líquido do mês: ', str(salario_liquido) + ' R$', '\n==========================//==========================')