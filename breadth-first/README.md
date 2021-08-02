# Challenge Summary
write a breadth first function that takes a graph and returns a collection of nodes in the order they were visited.


## Whiteboard Process
![img](code36.png)

## Approach & Efficiency
o(n^2)

## Solution

```
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


```
