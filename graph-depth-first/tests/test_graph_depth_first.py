from graph_depth_first import __version__
from graph_depth_first.depth_first import Graph


def test_version():
    assert __version__ == '0.1.0'

def test_one():
    g=Graph()
    g.addEdge('a', 'b')
    g.addEdge('a', 'd')
    g.addEdge('b', 'c')
    g.addEdge('c', 'g')
    g.addEdge('b', 'd')
    g.addEdge('d', 'e')
    g.addEdge('d', 'h')
    g.addEdge('d', 'f')
    g.addEdge('f', 'h')
    assert g.DFS('a')== {'a', 'b', 'c','g', 'd', 'e','h' ,'f'}

def test_tow():
    g=Graph()
    g.addEdge('d', 'e')
    g.addEdge('d', 'h')
    g.addEdge('d', 'f')
    g.addEdge('f', 'h')
    assert g.DFS('d')== {'d', 'e', 'f', 'h'}


def test_three():
    g=Graph()
    g.addEdge('b', 'c')
    g.addEdge('c', 'g')
    g.addEdge('b', 'd')
    g.addEdge('d', 'e')
    g.addEdge('d', 'h')
    g.addEdge('d', 'f')
    g.addEdge('f', 'h')
    assert g.DFS('b')== { 'b', 'c','g', 'd', 'e','h' ,'f'}

def test_three():
    g=Graph()
    assert g.DFS('')== {''}



