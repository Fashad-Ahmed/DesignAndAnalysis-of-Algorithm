import timeit
from timeit import Timer

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
    return arr

if __name__ == "__main__":
    print('Before Sorting')
    array = [54,26,93,17,77,31,44,55,20]
    print(array)
    print('After Sorting')
    print('Sorted Array for Best Case is {}'.format(bubbleSort(array)))

    t1 = timeit.Timer("bubbleSort(" + str(array) + ")", "from __main__ import bubbleSort")
    print("Running Time of Bubble Sort :  ", t1.timeit(number=1000), "milliseconds")