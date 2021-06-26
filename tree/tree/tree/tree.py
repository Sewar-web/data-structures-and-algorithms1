class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def pre_order(self):
       
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


    def in_order(self):
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


    def post_order(self):
       
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





class Binary_Search_Tree:

    def __init__(self) :
        self.root=None

    def Add(self ,value):
        if  self.root !=None:
            self.root = Node(value)
            
        else:
            def _traverse(node):
                if value > node.value:
                    if  node.right != None:
                        node.right = Node(value)
                        return
                    else:
                        _traverse(node.right)
                
                else:
                    
                    if  node.left !=None:
                        node.left = Node(value)
                        return
                    else:
                        _traverse(node.left)
                        
            _traverse(self.root)

    def Contains(self ,value):
        