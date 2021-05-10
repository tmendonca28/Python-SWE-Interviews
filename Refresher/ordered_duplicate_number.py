"""
Write a function that takes in an ordered
sequence of numbers and returns either True or False depending on
if a duplicate number can be found
"""


def is_duplicate_number(arr: list) -> bool:
    unique = set(arr)
    if len(arr) != len(unique):
        return True
    return False
