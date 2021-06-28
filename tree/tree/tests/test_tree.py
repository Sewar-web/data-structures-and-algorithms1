from tree.tree import Node ,Binary_Tree , Binary_Search_Tree
from tree import __version__


def test_version():
    assert __version__ == '0.1.0'


import pytest

def test_version():
    assert __version__ == '0.1.0'

#////////////////////////////////////pre_order/////////////////////////////////////////////


def test_pre_order(prepared_tree):
    assert prepared_tree.pre_order() == ['A', 'B', 'D', 'E', 'C', 'F']


def test_pre_order_empty_tree():
    tree = Binary_Tree()
    assert tree.pre_order() == []

#////////////////////////////////////in_order/////////////////////////////////////////////

def test_in_order(prepared_tree):
    assert prepared_tree.in_order() == ['D', 'B', 'E', 'A', 'F', 'C']

def test_in_order_empty_tree():
    tree = Binary_Tree()
    assert tree.in_order() == []


#////////////////////////////////////post_order/////////////////////////////////////////////


def test_post_order(prepared_tree):
    assert prepared_tree.post_order() == ['D', 'E', 'B', 'F', 'C', 'A']

def test_post_order_empty_tree():
    tree = Binary_Tree()
    assert tree.post_order() == []

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
    assert tree.pre_order()==[5, 1, 0, 4, 10, 7, 12]
    assert tree.in_order()==[0, 1, 4, 5, 7, 10, 12]
    assert tree.post_order()==[0, 4, 1, 7, 12, 10, 5]


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


#////////////////////////////////////Tree_is_empty/////////////////////////////////////////////


def test_tree_empty():
    tree = Binary_Tree()
    assert tree.pre_order() ==[]
    assert tree.in_order() ==[]
    assert tree.post_order() == []



#////////////////////////////////////Max_Value/////////////////////////////////////////////

def test_max_value():
    max=Binary_Tree()
    max.root = Node(10)
    max.root.right = Node(15)
    max.root.left = Node(11)
    max.root.right.left = Node(17)
    max.root.left.left = Node(20)
    max.root.right.right = Node(3)
    assert max.max_value() == 20



#///////////////////////////////////////////////breadth_first///////////////////

    breadth=Binary_Tree()
    breadth.root = Node(1)
    breadth.root.left = Node(2)
    breadth.root.right = Node(3)
    breadth.root.left.left = Node(4)
    breadth.root.right.left = Node(5)
    breadth.root.right.right = Node(6)
    assert breadth.breadth_first(breadth)==[1,2,3,4,5,6]








@pytest.fixture
def prepared_tree():
    tree = Binary_Tree()
    tree.root = Node('A')
    tree.root.left = Node('B')
    tree.root.right = Node('C')
    tree.root.left.left = Node('D')
    tree.root.left.right = Node('E')
    tree.root.right.left = Node('F')
    return tree