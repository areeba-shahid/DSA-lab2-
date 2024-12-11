import random
import time


def RandomArray(size):
    array = []
    for i in range(size):
        num = random.randint(0, 99)
        array.append(num)
    return array

def InsertionSort(array, start, end):
    for i in range(start + 1, end + 1):
        key = array[i]
        j = i - 1
        while j >= start and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


def Merge(array, p, q, r):
    n1 = q - p + 1  # Left half
    n2 = r - q      # Right half
    left = array[p:q + 1]
    right = array[q + 1:r + 1]

    i = 0  # Initial index of left subarray
    j = 0  # Initial index of right subarray
    k = p  # Initial index of merged subarray

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    # Copy remaining elements of left[] if any
    while i < n1:
        array[k] = left[i]
        i += 1
        k += 1

    # Copy remaining elements of right[] if any
    while j < n2:
        array[k] = right[j]
        j += 1
        k += 1


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



# Save sorted array to file
def save(array):
    with open("SortedHybridSort.csv", mode="a") as f:
        for i in array:
            f.write(str(i) + "\n")

array = RandomArray(30000)
start_time = time.time()


# Perform Hybrid Merge Sort
print(HybridMergeSort(array, 0, len(array) - 1))
end_time = time.time()
runtime = end_time - start_time
print("Runtime for hybrid merge sort is", runtime, "seconds")

# Save sorted array
save(array)




