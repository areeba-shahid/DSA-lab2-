                                 #  Problem 1
import random
array=[]
min = 0 
max = 99
def RandomArray(size):
     for i in range (0,size):
        num = random.randint(min,max)
        array.append(num)
         
     return array


def InsertionSort(array, start, end):
    for i in range(start + 1, end):
        key = array[i]
        j = i - 1
        while j >= start and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    
    return array
 
 
def Merge(array, p, q, r):
    n1 = q - p + 1  # Left half
    n2 = r - q      # Right half
    left = array[p:q + 1] 
    right = array[q + 1:r + 1]

    i = 0  # Index of left array
    j = 0  # Index of right array
    k = p  # Index of merged array

    # Merging the two halves
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    # Copy any remaining elements from the left array
    while i < n1:
        array[k] = left[i]
        i += 1
        k += 1

    # Copy any remaining elements from the right array
    while j < n2:
        array[k] = right[j]
        j += 1
        k += 1

# MergeSort function
def MergeSort(array, start, end):
    if start < end:
        mid = (start + end) // 2
        MergeSort(array, start, mid)
        MergeSort(array, mid + 1, end)
        Merge(array, start, mid, end)
    return array
 



def HybridMergeSort(array, start, end):
    if (end - start + 1) <= 20:
        InsertionSort(array, start, end)
    elif start < end:
        # Find the middle point
        mid = (start + end) // 2

        # Recursively sort first and second halves
        HybridMergeSort(array, start, mid)
        HybridMergeSort(array, mid + 1, end)

        # Merge the two halves
        Merge(array, start, mid, end)
    return array
 
 
def SelectionSort(array, start, end):
    for i in range(start, end + 1):
        # Find the minimum element in the unsorted part
        min_index = i
        for j in range(i + 1, end + 1):
            if array[j] < array[min_index]:
                min_index = j
        # Swap 
        array[i], array[min_index] = array[min_index], array[i]
        
def BubbleSort(array, start, end):
     for i in range (start,end):
        for j in range (start,end-1):
            if(array[j] > array[j+1]):
                array[j],array[j+1] = array[j+1],array[j]
                
                
     return array  

def ShuffleArray(array, start, end):
    for i in range(start, end + 1):
        rand_index = random.randint(start, end)
        array[i], array[rand_index] = array[rand_index], array[i] 
    return array