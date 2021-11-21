import timeit
from timeit import Timer

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        loc = i - 1
        while loc >= 0 and arr[loc] > key:
            arr[loc + 1] = arr[loc]
            loc -= 1
        arr[loc + 1] = key
    return arr


if __name__ == "__main__":
    print('Before Sorting')
    arr_best = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    arr_avg = [10, 20, 30, 40, 60, 50, 70, 80, 90, 100]
    arr_worst = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    print(arr_best), print(arr_avg), print(arr_worst)

    print('After Sorting')
    print('Sorted Array for Best Case is {}'.format(insertionSort(arr_best)))
    print('Sorted Array for Average Case is {}'.format(insertionSort(arr_avg)))
    print('Sorted Array for Worst Case is {}'.format(insertionSort(arr_worst)))

    t1 = timeit.Timer("insertionSort(" + str(arr_best) + ")", "from __main__ import insertionSort")
    print("Best Case Time Complexity :  ", t1.timeit(number=1000), "milliseconds")
    t2 = timeit.Timer("insertionSort(" + str(arr_avg) + ")", "from __main__ import insertionSort")
    print("Average Case Time Complexity :  ", t2.timeit(number=1000), "milliseconds")
    t3 = timeit.Timer("insertionSort(" + str(arr_worst) + ")", "from __main__ import insertionSort")
    print("Worst Case Time Complexity :  ", t3.timeit(number=1000), "milliseconds")
