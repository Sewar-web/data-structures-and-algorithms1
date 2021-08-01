from graphs import __version__
from graphs.graph import Vertix ,Edge,Graph


def test_version():
    assert __version__ == '0.1.0'


graph = Graph()
def test_add_node():
    graph.add_node('a')
    assert  graph.get_nodes()=={'a': []}

def test_edge():
    graph=Graph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_edge('a', 'b', 8)
    assert graph.get_neighbors('a') == 'a :edge--> b ... weight: 8'

def test_nodes():
    graph=Graph()
    graph.add_node('a')
    graph.add_node('b')
    assert graph.get_nodes() == {'a': [],'b': []}

def test_neighbor():
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.add_node('d')
    graph.add_node('b')

    graph.add_edge('a', 'b', 5)
    graph.add_edge('a', 'd', 3)
    graph.add_edge('b', 'd', 1)
    graph.add_edge('a', 'a', 2)
    assert graph.get_nodes() == {'a': [['b', 5], ['d', 3], ['a', 2]], 'b': [['d', 1]], 'c': [], 'd': []}


def test_size():
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.add_node('d')
    graph.add_node('e')
    assert graph.size() == 5

def test_one_node():
    graph.add_node('s')
    graph.add_edge('s','s')
    assert graph.get_neighbors('s') == 's :edge--> s ... weight: 1'


def test_empty_graph():
    graph = Graph()
    assert graph.get_nodes() == None
