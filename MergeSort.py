import random
import time


def RandomArray(size):
    array = []
    for i in range(size):
        num = random.randint(0, 99)
        array.append(num)
    return array

# Merge function
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
# Save sorted array to file
def save(array):
    with open("SortedMergeSort.csv", mode="a") as f:
        for i in array:
            f.write(str(i) + "\n")

array = RandomArray(30000)
start_time = time.time()


print(MergeSort(array, 0, len(array) - 1))

end_time = time.time()
runtime = end_time - start_time
print("Runtime for merge sort is", runtime, "seconds")

# Save sorted array
save(array)
