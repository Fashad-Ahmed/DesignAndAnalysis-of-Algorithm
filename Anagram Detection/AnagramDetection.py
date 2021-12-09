import timeit
from timeit import Timer
from itertools import permutations
import matplotlib.pyplot as plt


def CompareAnagram(val1, val2):
    """
        check to see that each character in the first
        string actually occurs in the second.
    """
    arr = list(val2)
    loc1 = 0
    flag = True

    while len(val1) > loc1 and flag:
        loc2 = 0
        occur = False

        while len(arr) > loc2 and not occur:
            if val1[loc1] == arr[loc2]:
                occur = True
            else:
                loc2 += 1

        if occur:
            arr[loc2] = None
        else:
            flag = False
        loc2 += 1
    return flag


def SortAnagram(val1, val2):
    """
        sorts the two values and compare the occurence
        of words.
    """
    arr1 = list(val1)
    arr2 = list(val2)

    arr1.sort()
    arr2.sort()

    loc = 0
    match = True
    while len(val1) > loc and match:
        if arr1[loc] == arr2[loc]:
            loc += 1
        else:
            match = False
    return match


def BruteForceAnagram(val1, val2):
    """
        Generate a list of all possible strings using the characters
        from first value and then see if second value occurs.
    """
    arr1 = [''.join(i) for i in permutations(val1)]
    arr2 = [val2]

    for i in arr1:
        if i == arr2[0]:
            return True


def CountAnagram(val1, val2):
    """
    Finds the occurrence of each letter in a word, increments that certain,
    performs this operation for each letter of both values and finally checks
    does the number of occurrences are identical or not.
    """
    arr1 = arr2 = [0]*26

    for i in range(len(val1)):
        loc = ord(val1[i]) - ord('a')
        arr1[loc] += 1

    for i in range(len(val2)):
        loc = ord(val2[i]) - ord('a')
        arr2[loc] += 1

    counter = 0
    flag = True
    while counter < 26 and flag:
        if arr1[counter] == arr2[counter]:
            counter += 1
        else:
            flag = False
    return flag

if __name__ == "__main__":
    t1 = timeit.Timer("CompareAnagram('heart', 'earth')", "from __main__ import CompareAnagram")
    print("Comparing each character in a string Approach #01   :    ", t1.timeit(number=1000), "milliseconds")

    t2 = timeit.Timer("SortAnagram('heart', 'earth')", "from __main__ import SortAnagram")
    print("Sort and Compare Approach #02                       :    ", t2.timeit(number=1000), "milliseconds")

    t3 = timeit.Timer("BruteForceAnagram('heart','earth')", "from __main__ import BruteForceAnagram")
    print("Brute Force Approach #03                            :    ", t3.timeit(number=1000), "milliseconds")

    t4 = timeit.Timer("CountAnagram('heart','earth')", "from __main__ import CountAnagram")
    print("Count and Compare Approach #04                      :    ", t4.timeit(number=1000), "milliseconds")

    x = [t2.timeit(number=1000), t2.timeit(number=1000), t3.timeit(number=1000), t4.timeit(number=1000)]
    plt.hist(x, bins=5)
    plt.show()