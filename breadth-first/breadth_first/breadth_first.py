from collections import defaultdict
class Graph:
 
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
      

    def breadthFirst(self,node):
        visited = [] 
        queue = []   
        visited.append(node)
        queue.append(node)

        while queue:
            s = queue.pop(0) 
            for neighbour in self.graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return visited




if __name__=='__main__':
    g = Graph()
    g.addEdge('a', 'd')
    g.addEdge('a', 'c')
    g.addEdge('b', 'd')
    g.addEdge('c', 'a')
    g.addEdge('c', 'd')
    g.addEdge('d', 'd')
    print(g.breadthFirst('a'))

