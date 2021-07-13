```
def QuickSort(arr, left, right):
    if left < right:
        
        position = Partition(arr, left, right)
        QuickSort(arr, left, position - 1)
        QuickSort(arr, position + 1, right)

def Partition(arr, left, right):
    
    pivot = arr[right]
    low = left - 1
    for i in range(left ,right):
        if arr[i] <= pivot:
            low +=1
            Swap(arr, i, low)

    Swap(arr, right, low + 1)
    return low + 1


def Swap(arr, i, low):
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp

```
Trace [8,4,23,42,16,15]

**Pass 1**


* In the first pass through of the quicksort, we evaluate the povit =15 
* we compare each   numbers  if less than povit  move to the  left side and the greater than  move to the right side 
* in left side the povit =4  4< = 8 true swap to the right 
* in right side the povit = 16 we star comper the number with the povit 23 < 16 true and to the end 
  

