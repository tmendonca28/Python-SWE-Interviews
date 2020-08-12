def getSublist():
    l = [1, 4, 9, 10, 23]
    l1 = l[:3]
    l2 = l[3:]
    return [l1, l2]


def AppendToList():
    l = [1, 4, 9, 10, 23]
    l.append(90)
    return l


def getAverage():
    l1 = [1, 4, 9, 10, 23]
    avg = sum(l1) / len(l1)
    return avg

print(getAverage())


def removeList():
    l1 = [1, 4, 9, 10, 23]
    l2 = [4, 9]
    return [x for x in l1 if x not in l2]

print(removeList())


def getSquare():
    l1 = [x*x for x in list(range(1, 11))]
    return l1


print(getSquare())