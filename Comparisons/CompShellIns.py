import timeit
from timeit import Timer
import matplotlib.pyplot as plt
import math
plt.rcParams['figure.figsize'] = [10, 6]

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        loc = i - 1
        while loc >= 0 and arr[loc] > key:
            arr[loc + 1] = arr[loc]
            loc -= 1
        arr[loc + 1] = key
    return arr

def shellSort(arr):
    size = len(arr)
    interval = size//2
    while interval > 0:
        for i in range(interval, size):
            temp = arr[i]
            x = i
            while x >= interval and arr[x-interval] > temp:
                arr[x] = arr[x-interval]
                x -= interval
            arr[x] = temp
        interval //= 2
    return arr

if __name__ == "__main__":
    print('Before Sorting')
    array = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(array)
    print('After Sorting')
    print('Sorted Array is {}'.format(shellSort(array)))

    t1 = timeit.Timer("insertionSort(" + str(array) + ")", "from __main__ import insertionSort")
    print("Running Time of Insertion Sort :  ", t1.timeit(number=1000), "milliseconds")

    t2 = timeit.Timer("shellSort(" + str(array) + ")", "from __main__ import shellSort")
    print("Running Time of Shell Sort :  ", t2.timeit(number=1000), "milliseconds")

    x = [t1.timeit(number=1000), t2.timeit(number=1000)]
    plt.hist(x, bins=5)
    plt.show()
