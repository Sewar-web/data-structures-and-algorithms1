from quick_sort import __version__
from quick_sort.quick_sort import QuickSort

def test_version():
    assert __version__ == '0.1.0'



def test_reverse_sorted():
    arr = [5,12,7,5,5,7]
    left = 0
    right = len(arr) - 1
    QuickSort(arr, left, right)
    assert arr == [5, 5, 5, 7, 7, 12]


def test_few_uniques():
    arr = [20,18,12,8,5,-2]
    left = 0
    right = len(arr) - 1
    QuickSort(arr, left, right)
    assert arr == [-2, 5, 8, 12, 18, 20]


def test_nearly_sorted():
    arr = [2,3,5,7,13,11]
    left = 0
    right = len(arr) - 1
    QuickSort(arr, left, right)
    assert arr == [2, 3, 5, 7, 11, 13]