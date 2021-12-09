import timeit
from timeit import Timer
from itertools import permutations


def hashFunc(key):
    h = 0
    for i in key:
        h += ord(i)
    return h % 10


class hashMap:
    def __init__(self):
        self.MAX = 100
        self.array = [None for i in range(self.MAX)]

    def hashFunc(self, key):
        h = 0
        for i in key:
            h += ord(i)
        print(h % self.MAX)
        return h % self.MAX

    def add(self, key, value):
        h = self.hashFunc(key)
        self.array[h] = value

    """
    for collision: Chaining is used!
    """
    def __getitem__(self, key):
        index = self.hashFunc(key)
        for i in self.array[index]:
            if i[0] == key:
                return i[1]

    def __setitem__(self, key, value):
        h = self.hashFunc(key)
        char = False
        for i,j in enumerate(self.array[h]):
            if len(j) == 2 and j[0] == key:
                self.array[h][i] = (key,value)
                char = True
        if not char:
            self.array.append((key,value))


    def __delitem__(self, key):
        index_arr = self.hashFunc(key)
        for x,y in enumerate(self.array[index_arr]):
            if y[0] == key:
                print(x,' deleted')
                del self.array[index_arr][x]
                
    def CompareAnagram(self, val1, val2):
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
        print(flag)


    def SortAnagram(self, val1, val2):

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
        print(match)


    def BruteForceAnagram(self, val1, val2):

        arr1 = [''.join(i) for i in permutations(val1)]
        arr2 = [val2]

        for i in arr1:
            if i == arr2[0]:
                print(True)


    def CountAnagram(self, val1, val2):
        
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

if __name__ == '__main__':
    hl = hashMap()
    hl.hashFunc('h')
    hl.add('e', 30)
    hl.add('a', 45)
    hl.add('r', 50)
    hl.add('t', 90)

    print('\n' + 'Hash Table')
    print(hl.array)

    hl.BruteForceAnagram('heart', 'earth')
    hl.CompareAnagram('heart', 'earth')
    hl.CountAnagram('heart', 'earth')
    hl.CompareAnagram('heart', 'earth')