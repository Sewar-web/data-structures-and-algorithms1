# Stacks and Queues
stack is a data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous.
they have two kinds
1. FIFO
2. LIFO

queue
1. FIFO
2. LILO


## Challenge
how to pop from stack and queue

## Approach & Efficiency
time o(1) space o(1)

## API

***for the Stack class:***

1. push: takes any value as an argument and adds a new node with that value to the top of the stack

2. pop: does not take any argument, removes the node from the top of the stack, and returns the node’s value.

3. peek : does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.

4. isEmpty : takes no argument, and returns a boolean indicating whether or not the stack is empty.

***for the Queue class:***

1. enqueue : takes any value as an argument and adds a new node with that value to the back of the queue

2. dequeue : does not take any argument, removes the node from the front of the queue, and returns the node’s value.

3. peek : does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue.

4. isEmpty : takes no argument, and returns a boolean indicating whether or not the queue is empty.