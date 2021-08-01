# Graphs

A graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.

## Challenge
 graph should be represented as an adjacency list, and should include the following methods:

 1. add edge
 2. add node
 3. get nodes
 4. get neighbors
 5. size

## Approach & Efficiency

1. add node => o(1)
2. add edge => o(n)
3. get nodes => o(1)
4. get neighbors => o(n)
5. size => o(1)
## API

**Add_Node()**

Adds a new node to the graph
Takes in the value of that node
Returns the added node

**Add_Edge()**

Adds a new edge between two nodes in the graph
Include the ability to have a “weight”
Takes in the two nodes to be connected by the edge
Both nodes should already be in the Graph


**Get_Nodes()**
Returns all of the nodes in the graph as a collection (set, list, or similar)

**Get_Neighbors()**
Returns a collection of edges connected to the given node
Takes in a given node
Include the weight of the connection in the returned collection


**Size()**
Returns the total number of nodes in the graph