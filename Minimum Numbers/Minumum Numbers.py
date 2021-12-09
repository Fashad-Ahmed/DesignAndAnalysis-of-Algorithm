import timeit
from timeit import Timer

"""
    Write two Python functions to find the minimum number in a list. 
    The first function should compare each number to every other number on the list O(n2). 
    The second function should be linear O(n).
"""

def QuadraticMin(arr):
    """
        Sorts the provided array in 0(n^2) time and returns
        the least value.
    """
    for i in range(1, len(arr)):
        min = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > min:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = min
    return arr[0]

def LinearMin(arr):
    """
        Sorts the provided array in 0(n) time and returns
        the least value.
    """
    min = arr[0]
    for i in range(len(arr)):
        if min > arr[i]:
            min = arr[i]
    return min

if __name__ == "__main__":

    t1 = timeit.Timer("QuadraticMin([5,6,8,3,9,8,6,3,6,20,55])", "from __main__ import QuadraticMin")
    print("O(n^2) Approach:  ", t1.timeit(number=1000), "milliseconds")

    t2 = timeit.Timer("LinearMin([5,6,8,3,9,8,6,3,6,20,55])", "from __main__ import LinearMin")
    print("O(n) Approach:    ", t2.timeit(number=1000), "milliseconds")