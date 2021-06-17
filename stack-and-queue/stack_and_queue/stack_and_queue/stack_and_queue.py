class Node:
    def __init__(self ,value) :
         self.value=value
         self.next=None


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
        # OR
        # return True if self.top is None else False
        # OR
        # if self.top is None:
        #     return True
        # return False




# If we use a list(array), easily do this:
# data = [3, -7, 'd']
# data.pop()
# data.append(5)
# data[-1]
# return if len(data) == 0

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


