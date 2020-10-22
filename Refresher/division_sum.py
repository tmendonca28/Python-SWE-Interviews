"""
Write a method that takes in an integer n, then iterates
through all the numbers from 0 to n, and returns the sum of
numbers divisible by 5 or 7
"""

def compute_division_sum(n : int) -> int:
    sum = 0
    for i in range(n+1):
        if i%5==0 or i%7==0:
            sum+=i
    return sum
    