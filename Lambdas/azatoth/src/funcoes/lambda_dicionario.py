
# Função lambda para gerenciar um dicionário de jogos
gerenciar_jogos = lambda acao, dicionario, chave, valor=None: {
    'adicionar': lambda: dicionario.update({chave: valor}),
    'deletar': lambda: dicionario.pop(chave, None),
}.get(acao, lambda: None)()