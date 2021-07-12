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



if __name__ == "__main__":
    merge = [8,4,23,42,16,15]
    Mergesort(merge)
    print(merge)


    merge2 = [20,18,12,8,5,-2]
    Mergesort(merge2)
    print(merge2)


    merge3 = [5,12,7,5,5,7]
    Mergesort(merge3)
    print(merge3)


    merge4 =[2,3,5,7,13,11]
    Mergesort(merge4)
    print(merge4)


