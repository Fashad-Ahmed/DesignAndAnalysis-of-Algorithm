import timeit
from timeit import Timer

"""
    Calculate the running time using the Python Time module for three
    different algorithms for calculating the sum of firstN given integers
    (with and without loop) as discussed in the class.
"""

def sumOfIntegars(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def sumOfInt(n):
    sum = 0
    for i in range(1, n+1):
        j = i
        sum = sum + j
    return sum

def sumOfN(n):
    return (n * (n + 1)) / 2

if __name__ == "__main__":

    t1 = timeit.Timer("sumOfIntegars(50)", "from __main__ import sumOfIntegars")
    print("Iterative Approach #01:  ", t1.timeit(number=1000), "milliseconds")

    t2 = timeit.Timer("sumOfInt(50)", "from __main__ import sumOfInt")
    print("Iterative Approach #02:  ", t2.timeit(number=1000), "milliseconds")

    t3 = timeit.Timer("sumOfN(50)", "from __main__ import sumOfN")
    print("Non-Iterative Approach:  ", t3.timeit(number=1000), "milliseconds")
