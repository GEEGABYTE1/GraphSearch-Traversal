
def dfs(graph, current_vertex, target, visited=None):
    if visited == None:
        visited = []
    visited.append(current_vertex)
    
    for neighbour in graph[current_vertex]:
        if not neighbour in visited:
            path = dfs(graph, neighbour, target, visited)

            if path == None:
                print(visited)
                
            
    
                
    
    