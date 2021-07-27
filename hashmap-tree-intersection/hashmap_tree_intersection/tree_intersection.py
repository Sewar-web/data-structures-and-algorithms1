class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Binary_Tree:
    def __init__(self):
        self.root = None
    
    

    def pre_order(self):
        output = []
        try: 
            
            if not self.root:
                return output


            def _traverse(node):
                nonlocal output 
                output.append(node.value) 

                if node.left:
                    _traverse(node.left)
        
                if node.right:
                    _traverse(node.right)
                return output
            _traverse(self.root)

            return output
        except:
            return "you have error with insertion by pre_order"


  

def tree_intersection(tree,tree1):
    output = []
    if tree.root and tree1.root:
        arr = tree.pre_order()
        arr1 = tree1.pre_order()

        set1 = set(arr1)
        for a in arr:
            if a in set1:
                output.append(a)
    return output 



if __name__ == "__main__":
    
    tree1=Binary_Tree()
    
    tree1.root = Node(150)
    tree1.root.right = Node(250)
    tree1.root.left = Node(100)
    tree1.root.right.left = Node(200)
    tree1.root.right.right = Node(350)
    tree1.root.right.right.left = Node(300)
    tree1.root.right.right.right = Node(500)
    tree1.root.left.left = Node(75)
    tree1.root.left.right = Node(160)
    tree1.root.left.right.left = Node(125)
    tree1.root.left.right.right = Node(175)



    tree2 = Binary_Tree()
    tree2.root = Node(42)
    tree2.root.right = Node(600)
    tree2.root.left = Node(100)
    tree2.root.right.left = Node(200)
    tree2.root.right.right = Node(350)
    tree2.root.right.right.left = Node(4)
    tree2.root.right.right.right = Node(500)
    tree2.root.left.left = Node(15)
    tree2.root.left.right = Node(160)
    tree2.root.left.right.left = Node(125)
    tree2.root.left.right.right = Node(175)
    print(tree_intersection(tree1,tree2))
