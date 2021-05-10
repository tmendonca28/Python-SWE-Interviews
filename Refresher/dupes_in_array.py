"""
Write a method that takes in a list of positive ints and
returns list of element that appears twice in order of the
first time it has been encountered
"""


def list_duplicate_numbers(arr: list) -> list:
    dupes = []

    for i in arr:
        if arr.count(i) > 1 and i not in dupes:
            dupes.append(i)
    return dupes
