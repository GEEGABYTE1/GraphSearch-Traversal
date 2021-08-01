# Graph Search Traversal
Graph Search Traversal Algorithms using Breadth-First Search and Depth-First Search

# BFS 

Breadth-First Traversal was made using an inverse `.pop()` method of the stack. Instead of popping the top, we pop from the bottom. We also reference a "target", which
actually isn't really a target; it's just the last vertex.


# DFS

Instead of using a queue, we used recursion. This just makes the algorithm easier to read. Works just like a depth-first search algorithm but instead of searching for a value,
everytime it reaches a vertex with no more edges (in this case, we would consider this the end), we return the path. 

# More information 

To create distinct paths, we pop the root vertex's first edge every iteration because the first vertex represents that we have already been through that path with the very node. Hence, to
create distinct paths, we must close the path of the previous node. This process keeps going until there are no more edges left in the dictionary.

Test inputs are located in `test.py`, with comments to indicate which input goes with which.

Made in Python 🐍
