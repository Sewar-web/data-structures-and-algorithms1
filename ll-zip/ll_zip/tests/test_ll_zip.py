import pytest
from ll_zip import __version__
from ll_zip.ll_zip import LinkedList
from ll_zip.ll_zip import zipLists 

def test_version():
    assert __version__ == '0.1.0'


def test_ll_zip_1(fixed_list_1,fixed_list_2):
    fixed_list_1.append(2)
    fixed_list_2.append(4)
    assert str(zipLists(fixed_list_1,fixed_list_2)) == '{1}->{5}->{3}->{9}->{2}->{4}->None'


def test_ll_zip_2(fixed_list_1,fixed_list_2):
    fixed_list_2.append(4)
    assert str(zipLists(fixed_list_1,fixed_list_2)) == '{5}->{1}->{9}->{3}->{4}->None'



def test_ll_zip_3(fixed_list_1,fixed_list_2):
    fixed_list_1.append(2)
    assert str(zipLists(fixed_list_1,fixed_list_2)) == '{1}->{5}->{3}->{9}->{2}->None'


@pytest.fixture
def fixed_list_1():
    ll1=LinkedList()
    ll1.append(1)
    ll1.append(3)
    
    return ll1 

@pytest.fixture
def fixed_list_2():
    ll2=LinkedList()
    ll2.append(5)
    ll2.append(9)

    return ll2