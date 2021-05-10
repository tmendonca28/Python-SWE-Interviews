"""
Write a method that takes in a string and returns the reverse
of that string.
"""


def reverse(input: str) -> str:
    if input:
        return input[::-1]
    return "You Have Input an Out of Bounds Value."
