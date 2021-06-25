class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):

        node = Node(value)
        if not self.head:
            self.head = node

        else:
            node.next = self.head
            self.head = node

    def append(self, value):

        node = Node(value)
        if not self.head:
            self.head = node

        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node

    def include(self, value):
 
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
                if(value == current.value):
                    return True
                else:
                    return False

    def insertAfter(self, value, newVal):
        current = self.head
        while current is not None:
            if value == current.value:
                break
            current = current.next
        if current is None:
            raise ValueError("node is not presesnt in LL")
        else:
            node = Node(newVal)
            node.next = current.next
            current.next = node

    def insertBefore(self, value, newVal):
        if self.head is None:
            raise ValueError("Linked List is empty!")
        if self.head.value == value:
            node = Node(newVal)
            node.next = self.head
            self.head = node
            return
        current = self.head
        while current.next is not None:
            print(current.next.value)
            if current.next.value == value:
                break
            current = current.next
        if current.next is None:
            raise ValueError("Node is not found!")
        else:
            node = Node(newVal)
            node.next = current.next
            current.next = node

    def getNth(self, value):
        try:
            current = self.head
            valuesarr = []
            while(current.next != None):
                valuesarr.append(current.value)
                current = current.next
            else:
                valuesarr.append(current.value)
            valuesarr.reverse()
            return valuesarr[value]
        except:
            return 'out of range'


    def __str__(self):
        current = self.head
        if not current:
            return 'None'
        else:
            res = ''
            while current.next != None:
                res = res + '{' + str(current.value) + '}' + '->'
                current = current.next
            else:
                res += '{' + str(current.value) + '}' + '->' + 'None'
            return res

    def __repr__(self):
        pass

def zip_ll(ll1,ll2):

    x =0
    y =0
    curr = ll1.head
    curr1 = ll2.head

    while curr:
        x += 1
        curr = curr.next
        if curr == None:
            break 
    while curr1:
        y += 1
        curr1 = curr1.next
        if curr1 == None:
            break 

    if y <= x:
        curr = ll1.head
        curr1 = ll2.head

    if x < y:
        head = ll2.head.value
        curr = ll2.head
        curr1 = ll1.head


    while curr != None or curr1 != None:

        if curr1 != None:
            temp = curr.next
            temp1 = curr1.next
            curr.next = curr1
            curr = curr.next
            if temp != None:
                curr.next = temp
                curr = curr.next
            curr1 = temp1
        

        if curr.next == None and curr1 == None:
            curr = curr.next

        if curr == None:
            if x < y:
                ll1.insert(head)
            return ll1

if __name__ == "__main__":
    ll1=LinkedList()
    ll1.append(15)
    ll1.append(13)
    ll1.append(17)
    print(ll1)

    ll2=LinkedList()
    ll2.append(10)
    ll2.append(20)
    ll2.append(30)
    print(ll2)

    print(zip_ll(ll1,ll2))