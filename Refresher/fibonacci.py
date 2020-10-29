"""
Write a method that takes in an integer and returns
the nth fib number
"""

def get_fibonacci(n : int) -> int:
    if n<0: 
        return -1
    elif n==0: 
        return 0
    # Second Fibonacci number is 1 
    elif n==1: 
        return 1
    else: 
        return get_fibonacci(n-1)+get_fibonacci(n-2) 