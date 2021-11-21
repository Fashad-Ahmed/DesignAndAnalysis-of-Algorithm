import timeit
from timeit import Timer

def factorial(num):
    if num == 1 or num == 0:
        return num
    else:
        return num * factorial(num - 1)


if __name__ == "__main__":
    num = int(input('Enter number: '))
    print('Factorial of number {} is {}'.format(num, factorial(num)))

    t1 = timeit.Timer("factorial(" + str(num) + ")", "from __main__ import factorial")
    print("Time Complexity of Factorial Recursive Function:  ", t1.timeit(number=1000), "milliseconds")