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


def isDivisible(x ,y):
    return x%y==0

print(isDivisible(4, 2))


def Fibonacci(n):
   if n <= 1:
       return n
   else:
       return(Fibonacci(n-1) + Fibonacci(n-2))


def sum_N_Numbers(n):
    if n <= 1:
        return n
    else:
        return n + sum_N_Numbers (n - 1)