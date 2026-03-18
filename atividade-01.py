from collections import deque
import heapq


def labirinto_para_grafo(labirinto, com_custo=False):
    grafo = {}
    inicio = None
    objetivo = None

    linhas = len(labirinto)
    colunas = len(labirinto[0])

    # movimentos possíveis: cima, baixo, esquerda, direita
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(linhas):
        for j in range(colunas):
            # ignora paredes
            if labirinto[i][j] != '#':
                no_atual = (i, j)
                grafo[no_atual] = []

                # guarda início e fim
                if labirinto[i][j] == 'S':
                    inicio = no_atual
                elif labirinto[i][j] == 'E':
                    objetivo = no_atual

                # procura vizinhos válidos
                for di, dj in direcoes:
                    ni = i + di
                    nj = j + dj

                    # verifica se está dentro dos limites
                    if 0 <= ni < linhas and 0 <= nj < colunas:
                        # verifica se não é parede
                        if labirinto[ni][nj] != '#':
                            if com_custo:
                                # para A*
                                grafo[no_atual].append(((ni, nj), 1))
                            else:
                                # para BFS
                                grafo[no_atual].append((ni, nj))

    return grafo, inicio, objetivo


def bfs(grafo, inicio, objetivo):
    """
    Busca em largura - encontra caminho mais curto em número de passos
    Retorna:
    - caminho encontrado
    - quantidade de nós expandidos
    """
    fronteira = deque([(inicio, [inicio])])
    explorados = set()
    nos_expandidos = 0

    while fronteira:
        no_atual, caminho = fronteira.popleft()

        if no_atual == objetivo:
            return caminho, nos_expandidos

        if no_atual not in explorados:
            explorados.add(no_atual)
            nos_expandidos += 1

            for vizinho in grafo[no_atual]:
                if vizinho not in explorados:
                    novo_caminho = caminho + [vizinho]
                    fronteira.append((vizinho, novo_caminho))

    return None, nos_expandidos


def heuristica_manhattan(no, objetivo):
    return abs(no[0] - objetivo[0]) + abs(no[1] - objetivo[1])


def a_estrela(grafo, inicio, objetivo, heuristica):
    """
    Busca A* - ótima e completa se h é admissível
    Retorna:
    - caminho encontrado
    - custo total
    - quantidade de nós expandidos
    """
    fronteira = [(heuristica(inicio, objetivo), 0, inicio, [inicio])]
    custos = {inicio: 0}
    expandidos = set()
    nos_expandidos = 0

    while fronteira:
        f, g, no_atual, caminho = heapq.heappop(fronteira)

        # evita expandir o mesmo nó mais de uma vez
        if no_atual in expandidos:
            continue

        expandidos.add(no_atual)
        nos_expandidos += 1

        if no_atual == objetivo:
            return caminho, g, nos_expandidos

        for vizinho, custo_aresta in grafo[no_atual]:
            novo_g = g + custo_aresta

            if vizinho not in custos or novo_g < custos[vizinho]:
                custos[vizinho] = novo_g
                novo_f = novo_g + heuristica(vizinho, objetivo)

                heapq.heappush(
                    fronteira,
                    (novo_f, novo_g, vizinho, caminho + [vizinho])
                )

    return None, float('inf'), nos_expandidos


# Labirinto
labirinto = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '.', '#', '#', '.', '.', '.'],
    ['#', '.', '.', '.', '#', '.', 'E']
]


grafo_bfs, inicio, objetivo = labirinto_para_grafo(labirinto, com_custo=False)
caminho_bfs, expandidos_bfs = bfs(grafo_bfs, inicio, objetivo)


grafo_a, inicio, objetivo = labirinto_para_grafo(labirinto, com_custo=True)
caminho_a, custo_a, expandidos_a = a_estrela(grafo_a, inicio, objetivo, heuristica_manhattan)

# 3. Compare: quantos nós cada um expandiu?
print(">BFS")
print("Caminho:", caminho_bfs)
print("Nós expandidos:", expandidos_bfs)

print("\n>A*")
print("Caminho:", caminho_a)
print("Custo total:", custo_a)
print("Nós expandidos:", expandidos_a)

print("\n>Comparação")
if expandidos_bfs < expandidos_a:
    print("BFS expandiu menos nós.")
elif expandidos_a < expandidos_bfs:
    print("A* expandiu menos nós.")
else:
    print("Os dois expandiram a mesma quantidade de nós.")
