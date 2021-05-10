"""
Write a method that finds a value in an ordered array of integers
and returns its position if it can be found else return that the
value has not been found. Search done using Linear Search Algorithm
"""


def linear_search(array: list, value: int) -> str:
    for i in range(len(array)):
        if value == array[i]:
            return f"The value has been found at position: {i}"
    return "Value has not been found."
