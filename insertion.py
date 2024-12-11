                        
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

def save(array):
    
   f = open (file="SortedInsertionSort.csv", mode="a")
   for i in array:
         f.write (str(i) + "\n")


        
import time
array = RandomArray(30000)
start_time = time.time()
print(InsertionSort(array,0, len(array)-1))
end_time = time.time()
runtime = end_time - start_time
print("Runtime for insertion sort is",runtime,"seconds")
save(array)



