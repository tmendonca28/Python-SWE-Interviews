def getSublist():
    full_list = [1, 4, 9, 10, 23]
    l1 = full_list[:3]
    l2 = full_list[3:]
    return [l1, l2]


def AppendToList():
    full_list = [1, 4, 9, 10, 23]
    full_list.append(90)
    return full_list


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


def getCubes():
    l1 = [x**3 for x in list(range(1, 21))]
    return l1


print(getCubes())


def listOfEvenOdds():
    l1 = [x for x in list(range(0, 21)) if x % 2 == 0]
    l2 = [x for x in list(range(0, 21)) if x % 2 == 1]
    return [l1, l2]


print(listOfEvenOdds())


def evenSquare():
    l1 = sum([x**2 for x in list(range(0, 21)) if x % 2 == 0])
    return l1


print(evenSquare())


def getSquareNotDivBy3():
    l1 = [x**2 for x in list(range(0, 21)) if x % 2 == 0 and x % 3 != 0]
    return l1


print(getSquareNotDivBy3())
