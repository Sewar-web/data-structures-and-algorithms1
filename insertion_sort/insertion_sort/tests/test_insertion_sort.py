from insertion_sort import __version__
from insertion_sort.insertion_sort import insertion_sort


def test_version():
    assert __version__ == '0.1.0'


def test_Reverse_sorted():
    arr=[20,18,12,8,5,-2]
    actuall= [-2, 5, 8, 12, 18, 20]
    insertion_sort(arr)
    assert arr==actuall


def test_Few_uniques():
    arr=[5,12,7,5,5,7]
    actuall= [5, 5, 5, 7, 7, 12]
    insertion_sort(arr)
    assert arr ==actuall


def test_Nearly_sorted():
    arr =[2,3,5,7,13,11]
    actuall= [2, 3, 5, 7, 11, 13]
    insertion_sort(arr)
    assert arr==actuall