from linked_list.linked_list import LinkedList, Node
from linked_list import __version__
from linked_list.linked_list import LinkedList

def test_version():
    assert __version__ == '0.1.0'

def test_Node_it():
    s = Node(7)
    assert s.value == 7
    assert s.next == None


def test_insert_it():
    ll=LinkedList()
    ll.insert(7)
    assert ll.head.value==7
    assert ll.head.next==None
    ll.insert(4)
    assert ll.head.value==4
    assert ll.head.next.value ==7

def test_append_it():
    ll=LinkedList()
    ll.append(5)
    assert ll.head.value==5
    ll.append(6)
    assert ll.head.next.value==6
    assert ll.head.next.next==None





def test_include_it():
    ll=LinkedList()
    assert ll.include(1)== False
    ll.append(7)
    assert ll.include(2)== False
    assert ll.include(7)== True


def test_str_it():

    ll=LinkedList()
    assert str(ll) is 'None'
    ll.append(5)
    assert str(ll) == '{5}->None'
    ll.append(3)
    assert str(ll) == '{5}->{3}->None'
    ll.append(1)
    assert str(ll) == '{5}->{3}->{1}->None'



def test_insertafter():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(2)
    ll.insertAfter(2, 5)
    assert ll.head.next.next.value == 5
    ll.insertAfter(1, 3)
    assert ll.head.next.value == 3

def test_insertbefor():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(2)
    ll.insertBefore(1, 5)
    assert ll.head.next.value == 1
    ll.insertBefore(2, 3)
    assert ll.head.next.next.value == 3




def test_getNth():
    ll = LinkedList()
    assert ll.getNth(1) == 'out of range'
    ll.append(2)
    assert ll.getNth(1) == 'out of range'
    ll.getNth(0) == 3
    ll.append(7)
    ll.insert('hjl')
    ll.append(8)
    assert ll.getNth(2) == 2
    assert ll.getNth(3) == 'hjl'
    assert ll.getNth(6) == 'out of range'
    assert ll.getNth(-1) == 'hjl'

