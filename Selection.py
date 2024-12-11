import random
import time


def SelectionSort(array, start, end):
    for i in range(start, end + 1):
        # Find the minimum element in the unsorted part
        min_index = i
        for j in range(i + 1, end + 1):
            if array[j] < array[min_index]:
                min_index = j
        # Swap 
        array[i], array[min_index] = array[min_index], array[i]


def RandomArray(size):
    array = []
    min_val = 0
    max_val = 99
    for _ in range(size):
        num = random.randint(min_val, max_val)
        array.append(num)
    return array


def save(array, filename="SortedSelectionSort.csv"):
    with open(filename, mode="w") as f:
        for num in array:
            f.write(f"{num}\n")


   
array = RandomArray(30000)

   
start_time = time.time()

    # Perform Selection Sort on the array
SelectionSort(array, 0, len(array) - 1)

   
end_time = time.time()
runtime = end_time - start_time

  
print(f"Runtime for selection sort is {runtime:.6f} seconds")

    # Save the sorted array in a csv file
save(array)
