import time                        
import random
array=[]
min = 0 
max = 99
def RandomArray(size):
     for i in range (0,size):
        num = random.randint(min,max)
        array.append(num)
         
     return array

               
def BubbleSort(array, start, end):
     for i in range (start,end):
        for j in range (start,end-1):
            if(array[j] > array[j+1]):
                array[j],array[j+1] = array[j+1],array[j]
                
                
     return array

def save(array):
    
   f = open (file="SortedBubbleSort.csv", mode="a")
   for i in array:
         f.write (str(i) + "\n")


        

array = RandomArray(30000)
start_time = time.time()
print(BubbleSort(array,0, len(array)-1))
end_time = time.time()
runtime = end_time - start_time
print("Runtime for bubble sort is",runtime,"seconds")
save(array)



