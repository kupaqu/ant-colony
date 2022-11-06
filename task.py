from graph import Node, Graph
from ant_colony import AntColony

n1 = Node("1")
n2 = Node("2")
n3 = Node("3")
n4 = Node("4")
n5 = Node("5")
n6 = Node("6")
n7 = Node("7")
n8 = Node("8")
n9 = Node("9")


w_graph = Graph.create_from_nodes([n1,n2,n3,n4,n5,n6,n7,n8,n9])
 
w_graph.connect_bilateral(n1, n2, 10)
w_graph.connect_bilateral(n1, n4, 8)
w_graph.connect_bilateral(n1, n3, 6)

w_graph.connect_bilateral(n2, n4, 5)
w_graph.connect_bilateral(n2, n7, 11)

w_graph.connect_bilateral(n3, n5, 3)

w_graph.connect_bilateral(n4, n5, 5)
w_graph.connect_bilateral(n4, n6, 7)
w_graph.connect_bilateral(n4, n7, 12)

w_graph.connect_bilateral(n5, n6, 9)
w_graph.connect_bilateral(n5, n9, 12)

w_graph.connect_bilateral(n6, n8, 8)
w_graph.connect_bilateral(n6, n9, 10)

w_graph.connect_bilateral(n7, n6, 4)
w_graph.connect_bilateral(n7, n8, 6)

w_graph.connect_bilateral(n8, n9, 15)

ant_colony = AntColony(w_graph.adj_M, 50, 10, 100, 0.8, alpha=1, beta=1)
shortest_path = ant_colony.run()
print ("shortest path: {}".format(shortest_path))