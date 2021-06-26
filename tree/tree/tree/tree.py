class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        try: 
            output = ''
            if not self.root:
                return output


            def _traverse(node):
                nonlocal output # Because output is not accessible
                output = output + str(node.value) # Root

                if node.left:
                    _traverse(node.left)
        
                if node.right:
                    _traverse(node.right)
                return output
            _traverse(self.root)

            return output
        except:
            return "you have error with insertion by pre_order"


    def in_order(self):
        try:
            output = ''
            if not self.root:
                return output

            def _traverse(node):
                nonlocal output
                if node.left:
                    _traverse(node.left)
                output = output + str(node.value)
                if node.right:
                    _traverse(node.right)
                return output
            _traverse(self.root)
            return output
        except:
            return "you have error with insertion by in_order"


    def post_order(self):
       try:
            output = ''
            if not self.root:
                return output
            def _traverse(node):
                nonlocal output 

                if node.left:
                    _traverse(node.left)
                if node.right:
                    _traverse(node.right)
                output = output + str(node.value)
                return output
            _traverse(self.root)

            return output
       except:
            return "you have error with insertion by post_order"




class Binary_Search_Tree(Tree):

    def __init__(self):
        super().__init__()
        

    def Add(self ,value):
        try:
            if  self.root == None :
                self.root = Node(value)
                
            else:
                def _traverse(node):
                    if value > node.value :
                        if  node.right == None:
                            node.right = Node(value)
                            return
                        else:
                            _traverse(node.right)
                    
                    else:
                        
                        if  node.left == None:
                            node.left = Node(value)
                            return
                        else:
                            _traverse(node.left)
                            
                _traverse(self.root)
        except:
            return "you have error with insertion value "


    def Contains(self ,value):
        try:

            if  self.root==None:
                return False

            else:
                node = self.root
                
                def _iscontains(node):
                    if value == node.value:
                        return True

                    elif value < node.value:
                        node = node.left

                        if node:
                            return _iscontains(node)

                    elif value > node.value:
                        node = node.right

                        if node:
                            return _iscontains(node)
                        
                if _iscontains(node) == True:
                    return True

                else:
                    return False

        except:
            return "you have error value"


if __name__=='__main__':
    tree = Binary_Search_Tree()
    tree.Add(5)
    tree.Add(10)
    tree.Add(1)

    tree.Add(7)
    tree.Add(4)
    tree.Add(12)
    tree.Add(0)

    print(tree.Contains(5))
    print(tree.Contains(30))
    print(tree.Contains(12))


    print(tree.pre_order())
    print(tree.in_order())
    print(tree.post_order())