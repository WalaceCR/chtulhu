# pede ao usuário o tamanho do arquivo em MB e a velocidade do link em Mbps
tamanho_arquivo = float(input("Digite o tamanho do arquivo (em MB): "))
velocidade_internet = float(input("Digite a velocidade do link de Internet (em Mbps): "))

# converte o tamanho do arquivo para megabits (Mbps)
tamanho_arquivo_mbps = tamanho_arquivo * 8

# calcula o tempo de download em minutos
tempo_download = tamanho_arquivo_mbps / velocidade_internet / 60

# exibe o resultado na tela
print(f"Tempo aproximado de download: {tempo_download:.2f} minutos")
