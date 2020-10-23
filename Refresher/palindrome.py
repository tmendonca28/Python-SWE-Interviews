"""
Write a method that checks if a given string is
a palindrome
"""

def is_palindrome(input: str) -> bool:
    if input:
        if input.lower() == input.lower()[::-1]:
            return True
    return False
