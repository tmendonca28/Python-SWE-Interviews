import math

def findGCD(a, b):
    return math.gcd(a, b)

print(findGCD(8, 12))


def calculateSinCosTan(x):
    sine = math.sin(x)
    cos = math.cos(x)
    tan = math.tan(x)
    return [sine, cos, tan]


print(calculateSinCosTan(0))


def findMaximum(x ,y):
    return max(x,y)

print(findMaximum(2, 3))