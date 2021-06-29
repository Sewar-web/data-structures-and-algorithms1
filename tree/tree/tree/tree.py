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
                nonlocal output # Because output is not accessible
                output.append(node.value) # Root

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
        output = []
        try:
            
            if not self.root:
                return output

            def _traverse(node):
                nonlocal output
                if node.left:
                    _traverse(node.left)
                output.append(node.value)
                if node.right:
                    _traverse(node.right)
                return output
            _traverse(self.root)
            return output
        except:
            return "you have error with insertion by in_order"


    def post_order(self):
       output = []
       try:
            if not self.root:
                return output
            def _traverse(node):
                nonlocal output 

                if node.left:
                    _traverse(node.left)
                if node.right:
                    _traverse(node.right)
                output.append(node.value)
                return output
            _traverse(self.root)
            return output
       except:
            return "you have error with insertion by post_order"

    def max_value(self):
    
        self.node=self.root
        self.max=self.root.value

        try:
            def _max(node):
                if self.max < node.value:
                    self.max=node.value

                if node.right:
                    _max(node.right)
                
                if node.left:
                    _max(node.left)
                
            _max(self.node)
            return self.max
            
        except:
            return "you have an error"
       
#///////////////////////////////////code challenge 17 ////////////////////////////////////////////
  
    def breadth_first(self , tree):

        queue=[]
        output=[]
        
        if self.root:
            queue.append(self.root) 
            while queue:
                    node = queue.pop(0)
                    output.append(node.value)

                    if node.left is not None:
                        queue.append(node.left)

                    if node.right is not None:
                        queue.append(node.right)

                    
                
            return output
        else:
            return 'the tree is empty '

#//////////////////////////////////////////////code challenge 18/////////////////////////////////////////////

def fizzbuzz(n):

    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)

def Fizz_Buzz_Tree(k_ary):

    tree = Binary_Tree()

    if  k_ary.root==True:
         return tree

    def _tree(current):

        node = Node(fizzbuzz(current.value))

        if current.left:
            node.left = _tree(current.left)
        if current.right:
            node.right = _tree(current.right)
        return node

    tree.root = _tree(k_ary.root)
    return tree

    



#///////////////////////////////////////////////////////////////////////////////////////////////////////////

class Binary_Search_Tree(Binary_Tree):

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
    tree.Add(50)

    print(tree.Contains(5))
    print(tree.Contains(30))
    print(tree.Contains(12))

    print('\n')
    print('/'*50)
    print(tree.pre_order())
    print(tree.in_order())
    print(tree.post_order())

    print('\n')
    print('/'*50) 
    max=Binary_Tree()
    max.root = Node(10)
    max.root.right = Node(15)
    max.root.left = Node(11)
    max.root.right.left = Node(17)
    max.root.left.left = Node(20)
    max.root.right.right = Node(3)
    print(max.max_value())

    print('\n')
    print('/'*50)
    breadth=Binary_Tree()
    breadth.root = Node(1)
    breadth.root.left = Node(2)
    breadth.root.right = Node(3)
    breadth.root.left.left = Node(4)
    breadth.root.right.left = Node(5)
    breadth.root.right.right = Node(6)
    print(breadth.breadth_first(breadth))

    
    print('\n')
    print('/'*50)



    fizzBuzz = Binary_Tree()
    fizzBuzz.root = Node(1)
    fizzBuzz.root.left = Node(5)
    fizzBuzz.root.right = Node(25)
    fizzBuzz.root.left.left = Node(2)
    fizzBuzz.root.left.right = Node(18)
    fizzBuzz.root.right.right = Node(15)
    print(Fizz_Buzz_Tree(fizzBuzz).pre_order())
    print(Fizz_Buzz_Tree(fizzBuzz).in_order())
    print(Fizz_Buzz_Tree(fizzBuzz).post_order())







