import timeit
from timeit import Timer

def selectionSort(arr):
    # size = len(arr)
    for i in range(len(arr)):
        maxIndex = i
        for j in range(i+1, len(arr)):
            if arr[maxIndex] > arr[j]:
                maxIndex = j
        arr[i], arr[maxIndex] = arr[maxIndex], arr[i]
    return arr

if __name__ == "__main__":
    print('Before Sorting')
    array = [54,26,93,17,77,31,44,55,20]
    print(array)
    print('After Sorting')
    print('Sorted Array is {}'.format(selectionSort(array)))

    t1 = timeit.Timer("selectionSort(" + str(array) + ")", "from __main__ import selectionSort")
    print("Running Time of Selection Sort :  ", t1.timeit(number=1000), "milliseconds")