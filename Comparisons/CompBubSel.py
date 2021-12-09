import timeit
from timeit import Timer
import matplotlib.pyplot as plt
import math
plt.rcParams['figure.figsize'] = [10, 6]

def selectionSort(arr):
    for i in range(len(arr)):
        maxIndex = i
        for j in range(i+1, len(arr)):
            if arr[maxIndex] > arr[j]:
                maxIndex = j
        arr[i], arr[maxIndex] = arr[maxIndex], arr[i]
    return arr

def bubbleSort(arr):
    for i in range(len(arr)):
        exchanges = True
        if (exchanges is True):
            exchanges = False
            for j in range(0, len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    exchanges = True
                    arr[j+1],arr[j] = arr[j],arr[j+1]
    return arr

    
if __name__ == "__main__":
    print('Before Sorting')
    array = [54,26,93,17,77,31,44,55,20]
    print(array)
    print('After Sorting')
    print('Sorted Array is {}'.format(selectionSort(array)))

    t1 = timeit.Timer("selectionSort(" + str(array) + ")", "from __main__ import selectionSort")
    print("Running Time of Selection Sort :  ", t1.timeit(number=1000), "milliseconds")

    t2 = timeit.Timer("bubbleSort(" + str(array) + ")", "from __main__ import bubbleSort")
    print("Running Time of Bubble Sort :  ", t2.timeit(number=1000), "milliseconds")

    x = [t1.timeit(number=1000), t2.timeit(number=1000)]
    plt.hist(x, bins=5)
    plt.show()
