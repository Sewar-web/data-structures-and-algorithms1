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

def zipLists(ll1,ll2):

    i =0
    j =0
    current1 = ll1.head
    current2 = ll2.head

    while current1:
        i += 1
        current1 = current1.next
        if current1 == None:
            break 
    while current2:
        j += 1
        current2 = current2.next
        if current2 == None:
            break 

    if j <= i:
        current1 = ll1.head
        current2 = ll2.head

    if i < j:
        head = ll2.head.value
        current1 = ll2.head
        current2 = ll1.head


    while current1 != None or current2 != None:

        if current2 != None:
            temp = current1.next
            temp2 = current2.next
            current1.next = current2
            current1 = current1.next
            if temp != None:
                current1.next = temp
                current1 = current1.next
            current2 = temp2
        

        if current1.next == None and current2 == None:
            current1 = current1.next

        if current1 == None:
            if i < j:
                ll1.insert(head)
            return ll1

if __name__ == "__main__":
    ll1=LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(2)

    print(ll1)

    ll2=LinkedList()
    ll2.append(5)
    ll2.append(9)
    ll2.append(4)
    ll2.append(8)

    print(ll2)

    print(zipLists(ll1,ll2))