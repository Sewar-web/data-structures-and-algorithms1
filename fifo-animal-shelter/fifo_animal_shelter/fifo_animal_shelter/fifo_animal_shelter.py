class Node:
    def __init__(self ,value) :
         self.value=value
         self.next=None

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


class AnimalShelter:
    """
    A class to adopt or donate animals (Cat's & Dog's)
    """

    def __init__(self):
        self.front = None
        self.queue = Queue()
    
    def __str__(self):
        current = self.queue.front
        items = []
        while current:
            items.append(str(current.value))
            current = current.next
        return "\n".join(items)

    def enqueue_animal(self, animal):

        if animal == 'Dog' or animal == 'Cat':
            print(f'Thanks for dropping off your {animal}')
            self.queue.enqueue(animal)
            return 
        raise Exception('Invalid entry. Only Dogs and Cats allowed')

    def dequeue_animal(self, pref = None):
        
        if pref == None:
            adopted = self.queue.dequeue()
            print(f'Congrats on our new adopted {adopted}')
            return adopted
        elif pref == 'Cat' or pref == 'Dog':
            current = self.queue.front
            while current.next is not None and current.next.value != pref:
                current = current.next
            if current.next is None:
                print (f'Sorry, we are out of {pref}\'s')
            else:
                print('current', current.next.value)
                adopted = current.next
                current.next = current.next.next
                return adopted
        else: 
            print(f'Sorry, don\'t have any {pref}\'s. We only have Cats & Dogs')
            return None




if __name__ == "__main__":

    animal_shelter = AnimalShelter()
    animal_shelter.enqueue_animal('Cat')
    animal_shelter.enqueue_animal('Cat')
    animal_shelter.enqueue_animal('Cat')
    animal_shelter.enqueue_animal('Dog')

    animal_shelter.dequeue_animal('Cat')
    animal_shelter.dequeue_animal('Dog')
    

    print(animal_shelter.__str__())
    