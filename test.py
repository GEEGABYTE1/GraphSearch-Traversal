from graph import Graph 
from vertex import Vertex 
from bfs import bfs 
from dfs import dfs


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



### BFS Traversal ###
'''
first_element = list(test_graph.graph_dict.keys())[0]
last_element = list(test_graph.graph_dict.keys())[-1]
lst = list(test_graph.graph_dict[first_element].edges.keys())

for i in range(len(lst)):
    first_edge = lst[0]
    if i == 0:
        pass 
    else:
        dictionary[first_element].pop(0)
        lst.pop(0)
    output = bfs(dictionary, first_element, last_element)
    '''
    
#########################

### DFS Traversal ###
'''
first_element = list(test_graph.graph_dict.keys())[0]
lst = list(test_graph.graph_dict[first_element].edges.keys())

for i in range(len(lst)):
    first_edge = lst[0]
    if i == 0:
        pass
    else:
        dictionary[first_element].pop(0)
        lst.pop(0)
    
    output = dfs(dictionary, first_element)
    print()
    '''
#########################

