import numpy as np

class Node:
    def __init__(self, data, indexloc=None):
        self.data = data
        self.index = indexloc # индекс в матрице смежности
    
    def __repr__(self):
        return self.data
    
class Graph:
    @classmethod
    def create_from_nodes(self, nodes):
        return Graph(len(nodes), len(nodes), nodes)
    
    def __init__(self, row, col, nodes=None):
        self.adj_M = np.ones(shape=(row, col)) * np.inf # матрица смежности
        self.nodes = nodes
        for i in range(len(self.nodes)):
            self.nodes[i].index = i

    def connect_unilateral(self, node1, node2, weight=1): # одностороннее соединение
        self.adj_M[node1.index][node2.index] = weight
    
    def connect_bilateral(self, node1, node2, weight=1): # одностороннее соединение
        self.adj_M[node1.index][node2.index] = weight
        self.adj_M[node2.index][node1.index] = weight
    
    def disconnect_unilateral(self, node1, node2):
        self.adj_M[node1.index][node2.index] = 0
    
    def connect(self, node1, node2, weight=1): # двустороннее соединение
        self.connect_unilateral(node1, node2, weight)
        self.connect_unilateral(node2, node1, weight)

    def disconnect(self, node1, node2):
        self.disconnect_unilateral(node1, node2)
        self.disconnect_unilateral(node2, node1)

    def connections_from(self, node): # какие узлы указывают на данный узел
        connections = []
        for col in range(self.adj_M[node.index].shape[0]):
            if self.adj_M[node.index, col] != 0 or self.adj_M[node.index, col] != np.inf:
                connections.append((self.nodes[col], self.adj_M[node.index, col]))
        return connections
    
    def connections_to(self, node): # на какие узлы указывает данный узел
        connections = []
        for row in range(self.adj_M[:, node.index].shape[0]):
            if self.adj_M[row, node.index] != 0:
                connections.append((self.nodes[row], self.adj_M[row, node.index]))

    def is_connected(self, node1, node2):
        return self.adj_M[node1.index, node2.index] != 0 or self.adj_M[node2.index, node1.index] != 0
    
    def get_weight(self, node1, node2):
        return self.adj_M[node1.index, node2.index]

    def add_node(self, node):
        self.nodes.append(node)
        node.index = len(self.nodes)-1
        rows, cols = self.adj_M.shape
        new_adj_M = np.zeros(shape=(rows+1, cols+1))
        new_adj_M[:rows,:cols] = self.adj_M
        self.adj_M = new_adj_M
    
    def __repr__(self) -> str:
        return self.adj_M.__str__()