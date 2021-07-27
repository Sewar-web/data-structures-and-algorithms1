from hashmap_tree_intersection import __version__
from hashmap_tree_intersection.tree_intersection import Node,Binary_Tree,tree_intersection


def test_version():
    assert __version__ == '0.1.0'




def test_one():
    tree=Binary_Tree()
    
    tree.root = Node(150)
    tree.root.right = Node(250)
    tree.root.left = Node(100)
    tree.root.right.left = Node(200)
    tree.root.right.right = Node(350)
    tree.root.right.right.left = Node(300)
    tree.root.right.right.right = Node(500)
    tree.root.left.left = Node(75)
    tree.root.left.right = Node(160)
    tree.root.left.right.left = Node(125)
    tree.root.left.right.right = Node(175)



    tree1 = Binary_Tree()
    tree1.root = Node(42)
    tree1.root.right = Node(600)
    tree1.root.left = Node(100)
    tree1.root.right.left = Node(200)
    tree1.root.right.right = Node(350)
    tree1.root.right.right.left = Node(4)
    tree1.root.right.right.right = Node(500)
    tree1.root.left.left = Node(15)
    tree1.root.left.right = Node(160)
    tree1.root.left.right.left = Node(125)
    tree1.root.left.right.right = Node(175)
    expected=tree_intersection(tree,tree1)
    actuall=[100, 160, 125, 175, 200, 350, 500]
    assert expected == actuall




def test_tow_string():
    tree=Binary_Tree()
    
    tree.root = Node(150)
    tree.root.right = Node(250)
    tree.root.left = Node('sewar')
    tree.root.right.left = Node('ahmad')
    tree.root.right.right = Node(350)
    tree.root.right.right.left = Node(300)
    tree.root.right.right.right = Node('maqableh')
    tree.root.left.left = Node(75)
    tree.root.left.right = Node(160)




    tree1 = Binary_Tree()
    tree1.root = Node(42)
    tree1.root.right = Node(600)
    tree1.root.left = Node('sewar')
    tree1.root.right.left = Node('ahmad')
    tree1.root.right.right = Node(350)
    tree1.root.right.right.left = Node(4)
    tree1.root.right.right.right = Node('maqableh')
    tree1.root.left.left = Node(15)
    tree1.root.left.right = Node(160)

    expected=tree_intersection(tree,tree1)
    actuall=['sewar', 160, 'ahmad', 350, 'maqableh']
    assert expected == actuall

    

def test_three_empty():
    tree = Binary_Tree()
    tree1 = Binary_Tree()
    assert tree_intersection(tree,tree1) == []
