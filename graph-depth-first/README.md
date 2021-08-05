# Challenge Summary
write method depth first that print take one argument (graph) and print the node from depth first

## Whiteboard Process
![img](code38.png)

## Approach & Efficiency
o(n)
## Solution

```
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
```
