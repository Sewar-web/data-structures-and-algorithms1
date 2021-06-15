from ll_zip.ll_zip import ll_zip
from linked_list.linked_list import LinkedList
def test_one():
    ll1 = LinkedList()
    ll1.append(7)
    ll1.append(9)
    ll2 = LinkedList()
    ll2.append(1)

    actual = str(ll_zip(ll1,ll2))
    expected = f'{{7}}->{{1}}->{{9}}->None'
    assert actual==expected



def test_tow():
    ll1 = LinkedList()


    ll2 = LinkedList()
    ll2.append(9)
    ll2.append(7)

    actual = str(ll_zip(ll1,ll2))
    expected =f'{{9}}->{{7}}->None'
    assert actual==expected



def test_three():
    ll1 = LinkedList()
    ll1.append(7)
    ll2 = LinkedList()
    ll2.append(9)
    ll2.append(1)

    actual = str(ll_zip(ll1,ll2))
    expected = f'{{7}}->{{9}}->{{1}}->None'
    assert actual==expected


def test_four():
    ll1 = LinkedList()
    ll1.append(9)
    ll1.append(7)
    ll2 = LinkedList()
    

    actual = str(ll_zip(ll1,ll2))
    expected =f'{{9}}->{{7}}->None'
    assert actual==expected


def test_five():
    ll1 = LinkedList()


    ll2 = LinkedList()
    ll2.append(9)

    actual = str(ll_zip(ll1,ll2))
    expected =f'{{9}}->None'
    assert actual==expected


