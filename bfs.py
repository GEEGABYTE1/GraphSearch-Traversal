
def bfs(graph, start_vertex, target):
    path = [start_vertex]
    vertex_and_path = [start_vertex, path]
    bfs_queue = [vertex_and_path]
    visited = set()
    paths = {}
    counter = 0

    while bfs_queue:
        print('-'*24)
        current_vertex, path = bfs_queue.pop()
        visited.add(current_vertex)

        print(path)
        for neighbour in graph[current_vertex]:
            if not neighbour in visited:
                if neighbour == target:
                    path.append(neighbour)
                    bfs_queue.append([neighbour, path])
                    continue 
                else:
                    path.append(neighbour)
                    bfs_queue.append([neighbour, path])
        
        paths[counter] = path
        counter += 1
    
    #return paths 


        
    
    
            

    

