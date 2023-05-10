def inicializar_cache(tamanhoCache):
    cache = {}
    for index in range(tamanhoCache):
        cache[index] = -1
    return cache


outputCache = inicializar_cache(10)

def imprimir_cache(cache):
    print("Posição Cache\tPosição Memória")
    for chave, valor in cache.items():
        print(f"{chave}\t\t\t\t\t{valor}")


imprimir_cache(outputCache)


def mapeamento_direto(tamanho_cache, posicao_memoria):
    posicao_cache = posicao_memoria % tamanho_cache



