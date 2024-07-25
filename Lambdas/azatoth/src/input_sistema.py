from funcoes.lambda_dicionario import gerenciar_jogos

# Exemplo de uso
jogos = {}

# Adicionar jogos usando a função lambda
gerenciar_jogos('adicionar', jogos, '1', 'The Legend of Zelda')
gerenciar_jogos('adicionar', jogos, '2', 'Super Mario Bros.')

print(jogos)  # Saída: {'1': 'The Legend of Zelda', '2': 'Super Mario Bros.'}

# Deletar um jogo usando a função lambda
gerenciar_jogos('deletar', jogos, '1')

print(jogos)  # Saída: {'2': 'Super Mario Bros.'}