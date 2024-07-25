import pytest
from src.funcoes.lambda_dicionario import gerenciar_jogos

# Testes unitários usando pytest
def test_adicionar_jogo():
    jogos = {}
    gerenciar_jogos('adicionar', jogos, '1', 'The Legend of Zelda')
    assert jogos == {'1': 'The Legend of Zelda'}

def test_deletar_jogo():
    jogos = {'1': 'The Legend of Zelda'}
    gerenciar_jogos('deletar', jogos, '1')
    assert jogos == {}

def test_adicionar_e_deletar():
    jogos = {}
    gerenciar_jogos('adicionar', jogos, '1', 'The Legend of Zelda')
    gerenciar_jogos('adicionar', jogos, '2', 'Super Mario Bros.')
    gerenciar_jogos('deletar', jogos, '1')
    assert jogos == {'2': 'Super Mario Bros.'}

# Executar os testes
if __name__ == '__main__':
    pytest.main()
