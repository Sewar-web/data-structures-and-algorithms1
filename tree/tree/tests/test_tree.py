from tree.tree import Node ,Tree , Binary_Search_Tree
from tree import __version__


def test_version():
    assert __version__ == '0.1.0'


import pytest

def test_version():
    assert __version__ == '0.1.0'

#////////////////////////////////////pre_order/////////////////////////////////////////////


def test_pre_order(prepared_tree):
    assert prepared_tree.pre_order() == 'ABDECF'


def test_pre_order_empty_tree():
    tree = Tree()
    assert tree.pre_order() == ''

#////////////////////////////////////in_order/////////////////////////////////////////////

def test_in_order(prepared_tree):
    assert prepared_tree.in_order() == 'DBEAFC'

def test_in_order_empty_tree():
    tree = Tree()
    assert tree.in_order() == ''


#////////////////////////////////////post_order/////////////////////////////////////////////


def test_post_order(prepared_tree):
    assert prepared_tree.post_order() == 'DEBFCA'

def test_post_order_empty_tree():
    tree = Tree()
    assert tree.post_order() == ''

#////////////////////////////////////BTS/////////////////////////////////////////////



def test_BST():
    tree = Binary_Search_Tree()
    tree.add(5)
    tree.add(10)
    tree.add(1)

    tree.add(7)
    tree.add(4)
    tree.add(12)
    tree.add(0)
    assert tree.root.value == 5
    assert tree.root.left.value == 1
    assert tree.root.right.value == 10
    assert tree.root.left.left.value == 0
    assert tree.root.left.right.value == 4
    assert tree.root.right.left.value == 7
    assert tree.root.right.right.value == 12








@pytest.fixture
def prepared_tree():
    tree = Tree()
    tree.root = Node('A')
    tree.root.left = Node('B')
    tree.root.right = Node('C')
    tree.root.left.left = Node('D')
    tree.root.left.right = Node('E')
    tree.root.right.left = Node('F')
    return tree