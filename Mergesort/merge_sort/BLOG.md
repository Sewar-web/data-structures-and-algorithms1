```
def Mergesort(arr):
    n= len(arr)

    if n > 1:
        mid = int(n/2)
        left = arr[0:mid]
        right = arr[mid:n]
      
        Mergesort(left)
        
        Mergesort(right)
        
        Merge(left, right, arr)

def Merge(left, right, arr):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j +=  1
            
        k =k + 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


````


Trace [8,4,23,15]

mid=2
left = 8,4
right =23,15


**Pass 1**


In the first pass to combine the selection, we divide the array into two parts: left and right. We start from the left. If the number is less than the second, we save the first number with a variable and transfer the second to the first


**Pass 2**
In the first pass to combine the selection, we divide the array into two parts: left and right. We start from the left. If the number is less than the second, we save the first number with a variable and transfer the second to the first

**Pass 3**

Merge the two matrices together and make sure they are ordered
