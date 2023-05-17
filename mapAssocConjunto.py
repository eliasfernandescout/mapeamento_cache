posicoes_memoria = [0, 1, 2, 3, 4, 5, 6, 7]  # Exemplo de acesso em memória

# Mapeamento Associativo por Conjunto com tamanho de conjunto igual a 2 e técnica de substituição FIFO
tamanho_conjunto = 2
tecnica_substituicao = "FIFO"
mapeamento_associativo_conjunto(tamanho_conjunto, tecnica_substituicao, posicoes_memoria)
print("----------------------------------------")

# Mapeamento Associativo por Conjunto com tamanho de conjunto igual a 4 e técnica de substituição LFU
tamanho_conjunto = 4
tecnica_substituicao = "LFU"
mapeamento_associativo_conjunto(tamanho_conjunto, tecnica_substituicao, posicoes_memoria)
