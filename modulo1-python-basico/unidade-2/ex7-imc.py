import sys

altura = float(input('Digite sua altura: \n'))
peso = float(input('Digite seu peso: \n'))
idade_em_anos = int(input('Digite quantos anos você tem:\n'))

imc = 0.0
descritivo = ''

if idade_em_anos < 18:
    print('Teste para adultos')
    sys.exit()
else:
    imc = peso / (altura)**2
    if imc >= 18.5 or imc <= 25:
        descritivo = 'Peso normal'
    elif imc > 25 or imc <= 30:
        descritivo = 'Acima do peso'
    elif imc > 30:
        descritivo = 'Obeso'
    else:
        descritivo = 'Abaixo do peso'

print(f'Seu imc é de {imc:.2f}, portanto seu peso está {descritivo}')

#formatação :.2f de valores float

