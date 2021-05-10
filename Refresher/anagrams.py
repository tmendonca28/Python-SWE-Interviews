"""
Write a method that takes in 2 strings and checks whether they are anagrams
regardless of case sensitivity and spaces
"""


def are_anagrams(a: str, b: str) -> bool:
    return (sorted(a.replace(" ", "").lower()) ==
            sorted(b.replace(" ", "").lower()))
