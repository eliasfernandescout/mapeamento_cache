posicoes_memoria = [0, 1, 2, 3, 4, 5, 6, 7]  # Exemplo de acesso em memória

# Mapeamento Direto com tamanho de cache igual a 4
tamanho_cache = 4
mapeamento_direto(tamanho_cache, posicoes_memoria)
print("----------------------------------------")

# Mapeamento Associativo por Conjunto com tamanho de conjunto igual a 1 e técnica de substituição LRU
tamanho_conjunto = 1
tecnica_substituicao = "LRU"
mapeamento_associativo_conjunto(tamanho_conjunto, tecnica_substituicao, posicoes_memoria)
