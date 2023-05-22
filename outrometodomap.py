def adicionar_endereco(cache, endereco, tamanho_conjunto, tecnica_substituicao):
    conjunto = endereco % tamanho_conjunto
    bloco = endereco // tamanho_conjunto

    if bloco in cache[conjunto]:
        cache[conjunto].remove(bloco)
        cache[conjunto].append(bloco)
    else:
        if len(cache[conjunto]) < tamanho_conjunto:
            cache[conjunto].append(bloco)
        else:
            if tecnica_substituicao == "LRU":
                cache[conjunto].pop(0)
                cache[conjunto].append(bloco)
            elif tecnica_substituicao == "LFU":
                bloco_substituido = min(cache[conjunto], key=lambda x: cache[conjunto].count(x))
                cache[conjunto].remove(bloco_substituido)
                cache[conjunto].append(bloco)
            elif tecnica_substituicao == "FIFO":
                cache[conjunto].pop(0)
                cache[conjunto].append(bloco)


def mapeamento_associativo_conjunto(tamanho_cache, tamanho_conjunto, tecnica_substituicao, pos_memoria):
    cache = inicializar_cache(tamanho_cache)
    hits = 0
    misses = 0

    for endereco in pos_memoria:
        conjunto = endereco % tamanho_conjunto
        bloco = endereco // tamanho_conjunto

        if bloco in cache[conjunto]:
            hits += 1
        else:
            misses += 1

        adicionar_endereco(cache, endereco, tamanho_conjunto, tecnica_substituicao)
        print(f"Acesso: {endereco} -> Conjunto: {conjunto} -> Cache: {cache}")

    total_acessos = hits + misses
    taxa_hit = hits / total_acessos if total_acessos > 0 else 0.0

    print("\nResumo:")
    print(f"Total de posições de memórias acessadas: {total_acessos}")
    print(f"Total de hits: {hits}")
    print(f"Total de misses: {misses}")
    print(f"Taxa de cache hit: {taxa_hit:.2%}")


# Configuração de acesso em memória para mapeamento associativo por conjunto
posicoes_memoria = [0, 8, 16, 24, 32, 0, 4, 8, 12, 16, 20, 24]  # Exemplo de acesso em memória

tamanho_cache = 6
tamanho_conjunto = 2
tecnica_substituicao = "LRU"  # Pode ser "LRU", "LFU" ou "FIFO"

mapeamento_associativo_conjunto(tamanho_cache, tamanho_conjunto, tecnica_substituicao, posicoes_memoria)
