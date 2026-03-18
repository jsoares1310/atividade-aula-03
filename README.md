Atividade Prática 1: Resolver Labirinto
Implemente busca em labirinto:
labirinto = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '.', '#', '#', '.', '.', '.'],
    ['#', '.', '.', '.', '#', '.', 'E']
]
# S = início, E = fim, # = parede, . = caminho
# 1. Implemente BFS para encontrar caminho
# 2. Implemente A* com heurística Manhattan
# 3. Compare: quantos nós cada um expandiu?
Entrega: Código + comparação de desempenho entre BFS e A

Atividade Prática 2: Puzzle de 8 Peças
class Puzzle8:
 def __init__(self, estado_inicial):
 self.estado = estado_inicial # Lista 3x3
 def acoes_possiveis(self):
 """Retorna movimentos válidos do espaço vazio"""
 pass
 def aplicar_acao(self, acao):
 """Retorna novo estado após mover"""
 pass
 def heuristica_manhattan(self):
 """Soma das distâncias Manhattan"""
 pass
 def heuristica_pecas_erradas(self):
 """Conta peças fora do lugar"""
 pass
# Compare as duas heurísticas:
# - Quantos nós A* expande com cada uma?
# - Qual encontra solução mais rápido?
