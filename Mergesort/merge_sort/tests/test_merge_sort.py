from merge_sort import __version__
from merge_sort.merge_sort import Mergesort
def test_version():
    assert __version__ == '0.1.0'

def test_reverse_sorted():  
    arr=[20,18,12,8,5,-2]
    Mergesort(arr)
    assert arr == [-2, 5, 8, 12, 18, 20]

def test_few_uniques():  
    arr = [5,12,7,5,5,7]
    Mergesort(arr)
    assert arr == [5, 5, 5, 7, 7, 12]

def test_nearly_sorted():  
    arr = [2,3,5,7,13,11]
    Mergesort(arr)
    assert  arr == [2, 3, 5, 7, 11, 13]