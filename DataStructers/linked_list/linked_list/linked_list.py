class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


"""
Draft:
ll: head - None
ll.append(4)
ll: head - Node(4) -> None
ll.append(-1)
ll: head - Node(4) -> Node(-1) -> None
ll.append('s')
ll: head - Node(4) -> Node(-1) -> Node('s') -> None
"""


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        """
        Adds a node of a value to the head of LL
        """
        node = Node(value)
        if not self.head:
            self.head=node
        else:
           node.next= self.head
           self.head = node

        

    def append(self, value):
        """
        Adds a node of a value to the end of LL
        """
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node



    def include(self, value):
        """
        Return T/F if value is in the linked list or not
        """
        if not self.head:
            return False

        else:
            current = self.head
            while current.next != None:
                if(value != current.value):
                    current = current.next
                else:
                    return True
            else:
                if(value==current.value):
                    return True
                else:
                    return False


           


        
        
    
    def __str__(self):
        # "{ a } -> { b } -> { c } -> NULL"
        # Loop over all nodes
        # print all values in one line
        current = self.head
        if not current:
            return 'None'
        else :
            res=''
            while current.next != None:
                res=  res + '{' + str(current.value) +  '}' + '->' 
                current = current.next
            else:
                 res += '{' + str(current.value) +  '}' +  '->' + 'None' 
            return res


    def __repr__(self):
        pass

    


if __name__ == "__main__":
    # Instances of Node
    n1 = Node(35)
    n2 = Node('Sewar')
    n3 = Node(True)
    # print(n2.value)


    ll = LinkedList()
    ll.append(4)
    ll.insert(7)
    ll.append(5)
    ll.append(-1)
    

    print(ll.include(-1))
    

    print(str(ll))


    print(ll.head.value)
    print(ll.head.next.value)
    print(ll.head.next.next.value)
    print(ll.head.next.next.value)