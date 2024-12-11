import time
from funcs import InsertionSort, MergeSort, ShuffleArray

# Function to read words from a text file
def read_words(filename):
    words = []
    with open(filename, 'r') as file:
        for line in file:
            words.append(line.strip()) 
    return words

# Function to display runtime for sorting algorithms
def display_runtime(algorithm_name, runtime):
    print(f"{algorithm_name} runtime: {runtime} seconds")


words = read_words("words.txt")



start_time = time.time()
InsertionSort(words[:], 0, len(words) - 1)  
insertion_sort_time = time.time() - start_time


start_time = time.time()
MergeSort(words[:], 0, len(words) - 1)  
merge_sort_time = time.time() - start_time

# Display the runtime 

display_runtime("InsertionSort", insertion_sort_time)
display_runtime("MergeSort", merge_sort_time)

# Shuffle the words array using ShuffleArray
words2 = ShuffleArray(words, 0, len(words) - 1)

# Run InsertionSort on the shuffled list of words
start_time = time.time()
InsertionSort(words2[:], 0, len(words2) - 1) 
insertion_sort_time_shuffled = time.time() - start_time

# Run MergeSort on the shuffled list of words
start_time = time.time()
MergeSort(words2[:], 0, len(words2) - 1)  
merge_sort_time_shuffled = time.time() - start_time

# runtime for shuffled data
print("shuffled : ")
display_runtime("InsertionSort", insertion_sort_time_shuffled)
display_runtime("MergeSort", merge_sort_time_shuffled)


print('answer :  MergeSort would be a better option due to its more efficient time complexity.')