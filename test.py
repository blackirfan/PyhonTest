

def bubbleSort(array):
    n = len(array)

    for i in range(n):

        
        for j in range(0, n-i-1):

            
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]



array = [8,6,1,23,4,45,78,63,79,82]
 
bubbleSort(array)
 
print ("Sorted array is:")
for i in range(len(array)):
    print ("%d" %array[i])


     