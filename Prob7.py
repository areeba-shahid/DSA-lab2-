import time
import csv
from funcs import RandomArray, HybridMergeSort, SelectionSort, InsertionSort, BubbleSort, MergeSort

# Function to read the value of n from Nvalues.txt
def read_n_values(filename):
    n_values = []
    with open(filename, 'r') as file:
        for line in file:
            n_values.append(int(line.strip()))  # Strip newline and convert to int
    return n_values

# Function to save runtime data to a CSV file
def save_runtime_to_csv(filename, data):
    with open(filename, mode="w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["n", "InsertionMerge", "MergeSort", "HybridMergeSort","SelectionSort", "BubbleSort"])
        for row in data:
            writer.writerow(row)

# Main function to execute the sorting and measure runtime
def main():
    # Read the n values from Nvalues.txt
    n_values = read_n_values("Nvalues.txt")
    
    # Prepare to store runtime results
    runtime_results = []
    
    
   
    
    # Loop through each n value
    for n in n_values:
        # Generate a random array of size n
        array = RandomArray(n)

       

       

     
        start_time = time.time()
        InsertionSort(array[:], 0, len(array) - 1)  # Copy array
        insertion_sort_time = time.time() - start_time
        
        start_time = time.time()
        MergeSort(array[:], 0, len(array) - 1)  # Copy array
        merge_sort_time = time.time() - start_time
        
         # Measure runtime for HybridMergeSort
        start_time = time.time()
        HybridMergeSort(array[:], 0, len(array) - 1)  # Copy array to avoid sorting the same array
        hybrid_merge_sort_time = time.time() - start_time
        
        start_time = time.time()
        SelectionSort(array[:], 0, len(array) - 1)  # Copy array
        selection_sort_time = time.time() - start_time

            # Measure runtime for BubbleSort
        start_time = time.time()
        BubbleSort(array[:], 0, len(array) - 1)  # Copy array
        bubble_sort_time = time.time() - start_time

      
       

        # Append the results in the format: [n, HybridMergeSortTime, SelectionSortTime, InsertionSortTime, BubbleSortTime, MergeSortTime]
        runtime_results.append([n, insertion_sort_time, merge_sort_time,hybrid_merge_sort_time, selection_sort_time, bubble_sort_time])

    # Save the results in RunTime.csv
    save_runtime_to_csv("RunTime.csv", runtime_results)

if __name__ == "__main__":
    main()
