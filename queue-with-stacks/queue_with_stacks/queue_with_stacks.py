class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        
    def pop(self):
       try:
            temp=self.top
            if temp:
                    self.top = self.top.next
                    self.top.next == None
                    return temp.value
            else:
                    raise Exception ('Stack is Empty')
       except:
           return 'Stack is Empty'

           
    def peek(self):

        try:

            if self.top:
                 return self.top.value
            else:
                raise Exception ('Stack is Empty')

        except:
            return 'is empty'

    def is_empty(self): 
        return self.top == None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, value):
        node = Node(value)
        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):

        try:
            if self.front:
                temp = self.front
                temp2 = temp.next
                self.front = temp2
                return temp.value
            else:
                 raise Exception ('Queue is Empty')
        except:
            return('Queue is Empty')

    def peek(self):
        try:
            if self.front:
                return self.front.value
            else:
                raise Exception ('Queue is Empty')
        except:
            return 'is empty'

    def is_empty(self):
        return self.front==None


#//////////////////////////////////////// code challenge 11 /////////////////////////////////////////////////////#    

class PseudoQueue():
    def __init__(self):
        self.front = Stack()
        self.rear=Stack()

    def enqueue(self, value):
        return self.front.push(value)

    def dequeue(self):
     
       if  self.rear.is_empty():
            while self.front.top :
                push=self.rear.push
                push(self.front.pop())
       return self.rear.pop()
    





      

    
if __name__ == "__main__":
    pseudo = PseudoQueue()
    pseudo.enqueue(1)
    pseudo.enqueue(2)
    pseudo.enqueue(3)
    pseudo.enqueue(4)
    print('front---------      ',pseudo.front.top.value)
    print('dequeue1--------    ', pseudo.dequeue())
    pseudo.enqueue(7)
    print('add-------------    ',pseudo.front.top.value)
    print('dequeue2--------    ' ,pseudo.dequeue())
    print('dequeue3---------    '  ,   pseudo.dequeue())