def sumList(elem_list) -> int:
    return sum(elem_list)


print(sumList([1, 2, 3, 4, 5]))


def findMaximum(l):
    return max(l)

print(findMaximum([1, 4, 9, 10, 23]))


def findMaximumValueIndex(l):
    index = l.index(max(l))
    maximum = max(l)
    return [index,maximum]

print(findMaximumValueIndex([1, 4, 23, 10, 9]))


def reverseList(l):
    l.reverse()
    return l


print(reverseList(['Windows', 'macOS', 'Linux']))


def isSorted(l):
    return sorted(l) == l


print(isSorted([1, 2, 2, 3]))


def hasDuplicates(l):
    # returns true if there are duplicates
    return len(l) != len(set(l))


print(hasDuplicates([1, 2, 2, 3]))


def printEvenOdd(n):
    for num in reversed(range(1, n+1)):
        if num%2==0:
            print(f'Even number: {num}')
        else:
            print(f'Odd number: {num}')

printEvenOdd(10)