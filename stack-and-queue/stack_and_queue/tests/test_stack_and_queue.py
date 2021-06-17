from stack_and_queue.stack_and_queue import Node,Stack,Queue
from stack_and_queue import __version__
import pytest

def test_version():
    assert __version__ == '0.1.0'



def test_push():
    stack=Stack()
    stack.push(3)
    stack.push(-7)
    stack.push('d')
    actual = stack.top.value
    expected = 'd'
    assert actual == expected


def test_pop():
    stack = Stack()
    stack.push(3)
    stack.push(-7)
    stack.push('d')
    stack.pop()
    actual = stack.top.value
    expected = -7
    assert actual == expected
 
def test_peek():
    stack = Stack()
    stack.push(3)
    stack.push(-7)
    stack.push('d')
    actual = stack.top.value
    expected = 'd'
    assert actual == expected
    stack.push(3)
    stack.push(-7)
    stack.push('d')
    actual = stack.top.value
    expected = -7
    assert actual == expected

def test_is_empty():
    stack = Stack()
    stack.is_empty()
    actual = stack.top
    expected = None
    assert actual == expected


def test_enqueue():
    queue = Queue()
    queue.enqueue(8)
    queue.enqueue('hi')
    queue.enqueue(-4)
    queue.enqueue(6)
    actual = queue.front.value
    expected = 8
    assert actual == expected
    actual = queue.rear.value
    expected = 6
    assert actual == expected

def test_dequeue():
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    actual = queue.front.value
    expected = 2
    assert actual == expected
def test_dequeue1():
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.dequeue()
    actual = queue.front.value
    expected = 2
    assert actual == expected

def test_peek():
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    actual = queue.front.value
    expected = 1
    assert actual == expected

def test_is_empty():
    queue=Queue()
    queue.is_empty()
    actual = queue.front
    expected = None
    assert actual == expected

""" Notes
6 <- -4 <- 'hi' <- 8
                   F
R
"""


