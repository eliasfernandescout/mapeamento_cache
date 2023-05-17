from collections import deque


class CacheEntry:
    def __init__(self, endereco):
        self.endereco = endereco
        self.ultima_acesso = 0
        self.contagem_acessos = 0


class CacheSet:
    def __init__(self, tamanho_conjunto, tecnica_substituicao):
        self.tamanho_conjunto = tamanho_conjunto
        self.tecnica_substituicao = tecnica_substituicao
        self.conjunto = []
        self.contador_ultima_acesso = 0

    def adicionar_endereco(self, endereco):
        if endereco in self.conjunto:
            entry = next(entry for entry in self.conjunto if entry.endereco == endereco)
            entry.contagem_acessos += 1
            entry.ultima_acesso = self.contador_ultima_acesso
        else:
            if len(self.conjunto) < self.tamanho_conjunto:
                self.conjunto.append(CacheEntry(endereco))
            else:
                if self.tecnica_substituicao == "LRU":
                    entry = min(self.conjunto, key=lambda e: e.ultima_acesso)
                elif self.tecnica_substituicao == "LFU":
                    entry = min(self.conjunto, key=lambda e: e.contagem_acessos)
                elif self.tecnica_substituicao == "FIFO":
                    entry = self.conjunto[0]
                self.conjunto.remove(entry)
                self.conjunto.append(CacheEntry(endereco))
        self.contador_ultima_acesso += 1

    def imprimir_cache_set(self):
        print(f"Tamanho do conjunto: {self.tamanho_conjunto}")
        print(f"Técnica de substituição: {self.tecnica_substituicao}")
        print("Cache set:")
        for entry in self.conjunto:
            print(f"Endereço: {entry.endereco} | Última Acesso: {entry.ultima_acesso} | Contagem de Acessos: {entry.contagem_acessos}")


def mapeamento_associativo_conjunto(tamanho_conjunto, tecnica_substituicao, pos_memoria):
    cache_set = CacheSet(tamanho_conjunto, tecnica_substituicao)
    total_acessos = len(pos_memoria)
    total_hits = 0
    total_misses = 0

    for posicao in pos_memoria:
        cache_set.adicionar_endereco(posicao)

        if posicao in [entry.endereco for entry in cache_set.conjunto]:
            print(f"A posição de memória {posicao} está presente na cache.")
            print("Ocorreu um HIT.")
            total_hits += 1
        else:
            print(f"A posição de memória {posicao} não está presente na cache.")
            print("Ocorreu um MISS.")
            total_misses += 1

        cache_set.imprimir_cache_set()
        print()

    taxa_hit = total_hits / total_acessos if total_acessos > 0 else 0.0
    print("Resumo:")
    print(f"Total de posições de memórias acessadas: {total_acessos}")
    print(f"Total de hits: {total_hits}")
    print(f"Total de misses: {total_misses}")
    print(f"Taxa de cache hit: {taxa_hit:.2%}")


# Configuração de acesso em memória para mapeamento associativo por conjunto
posicoes_memoria = [0, 8, 16, 24, 32, 0, 4, 8, 12, 16, 20, 24]  # Exemplo de acesso em memória

tamanho_conjunto = 2
tecnica_substituicao = "LRU"  # Pode ser "LRU", "LFU" ou "FIFO"

mapeamento_associativo_conjunto(tamanho_conjunto, tecnica_substituicao, posicoes_memoria)


# posicoes_memoria = [0, 1, 2, 3, 4, 1, 2, 5, 6, 7]  # Exemplo de acesso em memória
#
# # Configuração 1 - Tamanho do conjunto: 2, Técnica de substituição: LRU
# tamanho_conjunto = 2
# tecnica_substituicao = "LRU"
# mapeamento_associativo_conjunto(tamanho_conjunto, tecnica_substituicao, posicoes_memoria)
# print("----------------------------------------")
#
# # Configuração 2 - Tamanho do conjunto: 2, Técnica de substituição: LFU
# tamanho_conjunto = 2
# tecnica_substituicao = "LFU"
# mapeamento_associativo_conjunto(tamanho_conjunto, tecnica_substituicao, posicoes_memoria)
# print("----------------------------------------")
#
# # Configuração 3 - Tamanho do conjunto: 2, Técnica de substituição: FIFO
# tamanho_conjunto = 2
# tecnica_substituicao = "FIFO"
# mapeamento_associativo_conjunto(tamanho_conjunto, tecnica_substituicao, posicoes_memoria)
