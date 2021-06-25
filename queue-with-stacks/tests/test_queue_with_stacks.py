from queue_with_stacks.queue_with_stacks import PseudoQueue
from queue_with_stacks import __version__


def test_version():
    assert __version__ == '0.1.0'

def test_enqueue():

    queue = PseudoQueue()
    queue.enqueue(1)
    assert queue.front.top.value == 1
    queue.enqueue(3)
    assert queue.front.top.value == 3



def test_dequeue():
    queue = PseudoQueue()
    assert queue.dequeue() == 'Stack is Empty'
    queue.enqueue(5)
    queue.enqueue(7)
    queue.enqueue(9)
    assert queue.front.top.value == 9
    assert queue.dequeue() == 'Stack is Empty'
    assert queue.dequeue() == 7

