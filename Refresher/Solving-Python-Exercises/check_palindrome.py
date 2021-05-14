def is_palindrome(input: str) -> bool:
    if input.lower() == input.lower()[::-1]:
        return True
    return False
