from breadth_first import __version__
from breadth_first.breadth_first import Graph

def test_version():
    assert __version__ == '0.1.0'

def test_one():
    g = Graph()
    g.addEdge('a', 'd')
    g.addEdge('a', 'c')
    g.addEdge('b', 'd')
    g.addEdge('c', 'a')
    g.addEdge('c', 'd')
    g.addEdge('d', 'd')
    assert g.breadthFirst('a')==['a', 'd', 'c']


def test_tow():
    g = Graph()
    g.addEdge('a', 'd')
    g.addEdge('a', 'c')
    g.addEdge('b', 'd')
    g.addEdge('c', 'a')
    g.addEdge('c', 'd')
    g.addEdge('d', 'd')
    assert g.breadthFirst('b')==['b', 'd']


def test_three():
    g = Graph()
    g.addEdge('a', 'd')
    g.addEdge('a', 'c')
    g.addEdge('b', 'd')
    g.addEdge('c', 'a')
    g.addEdge('c', 'd')
    g.addEdge('d', 'd')
    assert g.breadthFirst('d')==['d']










