def lengthDictionary(Students):
    return len(Students)

Students = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas":  10
}

print(lengthDictionary(Students))


def calcAvg(Students):
    return (sum(Students.values()) / len(Students))


print(calcAvg(Students))


def oldestStudent(Students):
    return max(Students, key = Students.get)


print(oldestStudent(Students))


def updateAges(Students, n):
    Students = {k:v+n for k,v in Students.items()}
    return Students

print(updateAges(Students, 1))