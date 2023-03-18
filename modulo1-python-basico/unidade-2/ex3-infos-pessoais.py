nome = input('Digite seu nome\n')
estado_civil = input('Digite seu estado civil\n')
genero = input('Digite seu gênero\n')

if (genero.upper() == 'F') and (estado_civil.upper() == 'CASADA'):
    tempo_casamento = input(f'Olá {nome}, peço que informe quanto tempo está casada\n')
    print(f'Nome: {nome}\nGênero: {genero}\nEstado civil: {estado_civil}\nAnos de casamento: {tempo_casamento}')