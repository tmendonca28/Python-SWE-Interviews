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