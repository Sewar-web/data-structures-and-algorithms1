class Vertix:
    def __init__(self, value):
        self.value = value


class Edge():
    def __init__(self, vertix, weight=None):
        self.vertix = vertix
        self.weight = weight


class Graph():
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        node = Vertix(value)
        self.adjacency_list[node.value] = []
        return node.value

    def add_edge(self, start_node, end_node, weghit=None):
        if start_node and end_node in self.adjacency_list:
            if weghit != None:
                self.adjacency_list[start_node].append(Edge(end_node, weghit))
            else:
                self.adjacency_list[start_node].append(Edge(end_node))

    def get_nodes(self):
        if self._adjacency_list:
            return self._adjacency_list

    def get_neighbors(self, node):
        return self.adjacency_list[node]

    def size(self):
        return len(self.adjacency_list)

    def business_trip(graph,Cname):
        cost=0
        flag=False

        for cn in range(len(Cname)-1):
            edge=graph.get_neighbors(Cname[cn])
            for e in edge:
                if Cname[cn+1]==e.vertix:
                    cost+=e.weight
                    flag=True
        
        if flag==False:
            cost=0
            flag=False
            return f'{flag},${cost}'


        return f'{flag},${cost}'


if __name__=="__main__":
    g=Graph()
   
    a=g.add_node('Pandora')
    b=g.add_node('Arendelle')
    c=g.add_node('Metroville')
    d=g.add_node('Monstropolis')
    e=g.add_node('Naboo')
    f=g.add_node('Narnia')

    g.add_edge(a,b,150)
    g.add_edge(a,c,82)   
    g.add_edge(b,c,99)
    print(g.business_trip([a,b]))
    print(g.business_trip([a,f]))


  