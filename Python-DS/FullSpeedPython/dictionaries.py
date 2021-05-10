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
    return max(Students, key=Students.get)


print(oldestStudent(Students))


def updateAges(Students, n):
    Students = {k: v+n for k, v in Students.items()}
    return Students


print(updateAges(Students, 1))


def totalStudents(Students):
    return len(Students.keys())


print(totalStudents(Students))


def calcAverageAge(Students):
    sum_age = 0
    for k, v in Students.items():
        sum_age += v["age"]
    return sum_age/len(Students)


def find_students(students, address):
    cities = []
    for k, v in students.items():
        if v["address"] == address:
            cities.append(k)

    return sorted(cities)
