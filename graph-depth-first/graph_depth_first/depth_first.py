from collections import defaultdict
class Graph:
 
   
    def __init__(self):
 
        
        self.graph = defaultdict(list)
 
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    
    def DFSUtil(self, v, visited):
            visited.add(v)
            print(v, end=' ')
            for neighbour in self.graph[v]:
                if neighbour not in visited:
                    self.DFSUtil(neighbour, visited)
           

    def DFS(self, v):
    
        visited = set()
        self.DFSUtil(v, visited)
        return visited
        
        
 

g = Graph()
g.addEdge('a', 'b')
g.addEdge('a', 'd')
g.addEdge('b', 'c')
g.addEdge('c', 'g')
g.addEdge('b', 'd')
g.addEdge('d', 'e')
g.addEdge('d', 'h')
g.addEdge('d', 'f')
g.addEdge('f', 'h')
g.DFS('a')