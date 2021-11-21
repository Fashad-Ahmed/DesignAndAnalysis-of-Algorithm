import timeit
from timeit import Timer

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
        while i < len(left) and j > len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

if __name__ == "__main__":
    print('Before Sorting')
    arr_best = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    arr_avg = [10, 20, 30, 40, 60, 50, 70, 80, 90, 100]
    arr_worst = [100, 90, 80, 70, 60, 50, 40, 30, 10, 20]
    print(arr_best), print(arr_avg), print(arr_worst)

    print('After Sorting')
    print('Sorted Array for Best Case is {}'.format(mergeSort(arr_best)))
    print('Sorted Array for Average Case is {}'.format(mergeSort(arr_avg)))
    print('Sorted Array for Worst Case is {}'.format(mergeSort(arr_worst)))

    t1 = timeit.Timer("mergeSort(" + str(arr_best) + ")", "from __main__ import mergeSort")
    print("Best Case Time Complexity :  ", t1.timeit(number=1000), "milliseconds")
    t2 = timeit.Timer("mergeSort(" + str(arr_avg) + ")", "from __main__ import mergeSort")
    print("Average Case Time Complexity :  ", t2.timeit(number=1000), "milliseconds")
    t3 = timeit.Timer("mergeSort(" + str(arr_worst) + ")", "from __main__ import mergeSort")
    print("Worst Case Time Complexity :  ", t3.timeit(number=1000), "milliseconds")
