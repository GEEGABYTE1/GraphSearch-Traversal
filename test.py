from graph import Graph 
from vertex import Vertex 


test_graph = Graph()

one = Vertex(1)
two = Vertex(2)
three = Vertex(3)
four = Vertex(4)
five = Vertex(5)
six = Vertex(6)

test_graph.add_vertex(one)
test_graph.add_vertex(two)
test_graph.add_vertex(three)
test_graph.add_vertex(four)
test_graph.add_vertex(five)
test_graph.add_vertex(six)

# Test Graph #

test_graph.add_edge(one, two)
test_graph.add_edge(one, three)
test_graph.add_edge(one, five)
test_graph.add_edge(two, three)
test_graph.add_edge(three, four)
test_graph.add_edge(three, five)
test_graph.add_edge(four, six)
test_graph.add_edge(four, five)
test_graph.add_edge(five, six)



dictionary = {}

for vertex, edge in test_graph.graph_dict.items():
    edges = list(edge.edges.keys())
    dictionary[vertex] = edges 

print(dictionary)
