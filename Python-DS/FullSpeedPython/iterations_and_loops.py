def sumList(elem_list) -> int:
    return sum(elem_list)


print(sumList([1, 2, 3, 4, 5]))


def findMaximum(query_list):
    return max(query_list)


print(findMaximum([1, 4, 9, 10, 23]))


def findMaximumValueIndex(query_list):
    index = query_list.index(max(query_list))
    maximum = max(query_list)
    return [index, maximum]


print(findMaximumValueIndex([1, 4, 23, 10, 9]))


def reverseList(query_list):
    query_list.reverse()
    return query_list


print(reverseList(['Windows', 'macOS', 'Linux']))


def isSorted(query_list):
    return sorted(query_list) == query_list


print(isSorted([1, 2, 2, 3]))


def hasDuplicates(query_list):
    # returns true if there are duplicates
    return len(query_list) != len(set(query_list))


print(hasDuplicates([1, 2, 2, 3]))


def printEvenOdd(n):
    for num in reversed(range(1, n+1)):
        if num % 2 == 0:
            print(f'Even number: {num}')
        else:
            print(f'Odd number: {num}')


printEvenOdd(10)
