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
    tree.Add(5)
    tree.Add(10)
    tree.Add(1)

    tree.Add(7)
    tree.Add(4)
    tree.Add(12)
    tree.Add(0)
    assert tree.pre_order()=='510410712'
    assert tree.in_order()=='014571012'
    assert tree.post_order()=='041712105'


#////////////////////////////////////BTS_Add/////////////////////////////////////////////


def test_BST_Add():
    tree = Binary_Search_Tree()
    tree.Add(5)
    tree.Add(10)
    tree.Add(1)

    tree.Add(7)
    tree.Add(4)
    tree.Add(12)
    tree.Add(0)
    assert tree.root.value == 5
    assert tree.root.left.value == 1
    assert tree.root.right.value == 10
    assert tree.root.left.left.value == 0
    assert tree.root.left.right.value == 4
    assert tree.root.right.left.value == 7
    assert tree.root.right.right.value == 12


#////////////////////////////////////BTS_Contains/////////////////////////////////////////////


def test_BST_Contains():
    tree = Binary_Search_Tree()
    tree = Binary_Search_Tree()
    tree.Add(5)
    tree.Add(10)
    tree.Add(1)
    tree.Add(7)
    tree.Add(4)
    tree.Add(12)
    tree.Add(0)
    assert tree.Contains(5) == True
    assert tree.Contains(10) == True
    assert tree.Contains(0) == True
    assert tree.Contains(12) == True


#////////////////////////////////////BTS_is_empty/////////////////////////////////////////////


def test_tree_empty():
    tree = Tree()
    assert tree.pre_order() == ''
    assert tree.in_order() == ''
    assert tree.post_order() == ''







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