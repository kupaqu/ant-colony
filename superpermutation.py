from graph import Node, Graph
import numpy as np
from ant_colony import AntColony

# функция генерирующая перестановки
def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
       m = lst[i]
       remLst = lst[:i] + lst[i+1:]
       for p in permutation(remLst):
           l.append([m] + p)
    return l

# расстояние между перестановками
def superpermutation_dist(a: str, b: str):
    if len(a) != len(b):
        raise('Different length of strings in permutations!')
    
    for i in range(len(a)):
        if a[i:] == b[:len(a)-i]:
            return i
    
    return len(a)

# генерация перестановок
data = list('123')
perm = permutation(data)

# генерация узлов перестановок
nodes = []
for i in range(len(perm)):
    nodes.append(Node(''.join(map(str, perm[i]))))

# создание полносвязного графа
graph = Graph.create_from_nodes(nodes)
for i in range(len(nodes)):
    for j in range(len(nodes)):
        if i == j:
            continue
        graph.connect_unilateral(nodes[i], nodes[j], superpermutation_dist(nodes[i].data, nodes[j].data))

# муравьиный алгоритм
ant_colony = AntColony(graph.adj_M, 50, 10, 50, 0.8, alpha=1, beta=1)
shortest_path = ant_colony.run()
# print (f'{shortest_path}')

# вывод кратчайшей найденной суперперестановки
prev = nodes[shortest_path[0][0][0]].data
for i in range(len(shortest_path[0])-1):
    src, dst = shortest_path[0][i]
    dist = superpermutation_dist(nodes[src].data, nodes[dst].data)
    # print(nodes[src].data, nodes[dst].data, dist)
    prev += nodes[dst].data[-dist:]

print(f'superpermutation length: {len(prev)}')
print(f'superpermutation: {prev}')