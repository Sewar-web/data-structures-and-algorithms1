class Vertix:
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return self.value


class Edge:
    def __init__(self ,vertix , weight) :
        self.vertix=vertix
        self.weight=weight
        
class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        v = Vertix(value)
        self._adjacency_list[v.value] = []
        return v


    def add_edge(self, start_node, end_node, weight=1):
        if start_node not in self._adjacency_list.keys():
            return
        elif end_node not in self._adjacency_list.keys():
            return
        else:
            edge = [end_node, weight]
            self._adjacency_list[start_node].append(edge)


    def get_nodes(self):
        if self._adjacency_list:
            return self._adjacency_list

    def get_neighbors(self, node):
        for edges in self._adjacency_list[node]:
            return f"{node} :edge--> {edges[0]} ... weight: {edges[1]}"

    def size(self):
        return len(self._adjacency_list)


