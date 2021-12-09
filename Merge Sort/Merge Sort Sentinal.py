import sys
SENTINEL = sys.maxsize
import timeit
from timeit import Timer

def merge(array, first, middle, last):
    n1 = middle - first + 1
    n2 = last - middle

    L = [None for t in range(n1 + 1)]
    R = [None for t in range(n2 + 1)]

    for i in range(n1):
        L[i] = array[first + i - 1]
    for j in range(n2):
        R[j] = array[middle + j]

    L[n1] = SENTINEL
    R[n2] = SENTINEL

    i = j = 0

    for k in range(first - 1, last):
        if L[i] <= R[j]:
            array[k] = L[i]
            i = i + 1
        else:
            array[k] = R[j]
            j = j + 1


def mergeSort(array, first, last):
    if first < last:
        middle = (first + last)//2
        mergeSort(array, first, middle)
        mergeSort(array, middle + 1, last)
        merge(array, first, middle, last)
    return array
if __name__ == "__main__":
    print('Before Sorting')
    arr_best = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    arr_avg = [10, 20, 30, 40, 60, 50, 70, 80, 90, 100]
    arr_worst = [100, 90, 80, 70, 60, 50, 40, 30, 10, 20]
    print(arr_best), print(arr_avg), print(arr_worst)

    print('After Sorting')
    print('Sorted Array for Best Case is {}'.format(mergeSort(arr_best, 1, len(arr_best))))
    print('Sorted Array for Average Case is {}'.format(mergeSort(arr_avg, 1, len(arr_avg))))
    print('Sorted Array for Worst Case is {}'.format(mergeSort(arr_worst, 1, len(arr_worst))))

    t1 = timeit.Timer("mergeSort(" + str(arr_best) + ",1,10)", "from __main__ import mergeSort")
    print("Best Case Time Complexity :  ", t1.timeit(number=1000), "milliseconds")
    t2 = timeit.Timer("mergeSort(" + str(arr_avg) + ",1,10)", "from __main__ import mergeSort")
    print("Average Case Time Complexity :  ", t2.timeit(number=1000), "milliseconds")
    t3 = timeit.Timer("mergeSort(" + str(arr_worst) + ",1,10)", "from __main__ import mergeSort")
    print("Worst Case Time Complexity :  ", t3.timeit(number=1000), "milliseconds")