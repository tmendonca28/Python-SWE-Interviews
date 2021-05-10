"""
Write a function that takes in a string and returns the number of vowels.
"""


def count_vowels(input: str) -> int:
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for i, v in enumerate(input):
        if v.lower() in vowels:
            count += 1
    return count
