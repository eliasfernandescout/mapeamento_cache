def mapeamento_direto(tamanho_cache, pos_memoria):
    cache = inicializar_cache(tamanho_cache)
    imprimir_cache(cache)
    total_acessos = len(pos_memoria)
    total_hits = 0
    total_misses = 0

    for posicao in pos_memoria:
        indice_cache = 0  # Sempre mapeia para a posição 0 da cache
        endereco_atual = cache[indice_cache]

        if endereco_atual == posicao:
            print(f"A posição de memória {posicao} está presente na cache.")
            print("Ocorreu um HIT.")
            total_hits += 1
        else:
            print(f"A posição de memória {posicao} não está presente na cache.")
            print("Ocorreu um MISS.")
            cache[indice_cache] = posicao
            total_misses += 1

        imprimir_cache(cache)
        print()

    taxa_hit = total_hits / total_acessos if total_acessos > 0 else 0.0
    print("Resumo:")
    print(f"Total de posições de memórias acessadas: {total_acessos}")
    print(f"Total de hits: {total_hits}")
    print(f"Total de misses: {total_misses}")
    print(f"Taxa de cache hit: {taxa_hit:.2%}")


# Funções auxiliares
def inicializar_cache(tamanho_cache):
    cache = {}
    for indice in range(tamanho_cache):
        cache[indice] = -1
    return cache


def imprimir_cache(cache):
    print(f"Tamanho da cache: {len(cache)}")
    print("Tabela:")
    for indice, valor in cache.items():
        print(f"Índice {indice}: {valor}")


# Configuração de acesso em memória para mapeamento direto
# posicoes_memoria = [0, 8, 16, 24, 32]  # Acesso a múltiplos de 8

posicoes_memoria = [1,6,1,11,1,16,1,21,1,26]
tamanho_cache = 8
mapeamento_direto(tamanho_cache, posicoes_memoria)
