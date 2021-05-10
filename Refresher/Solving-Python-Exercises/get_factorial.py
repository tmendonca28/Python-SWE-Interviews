# Get factorial of a given number


def get_factorial_of_number(number) -> int:
    if number == 1:
        return 1
    else:
        return number * get_factorial_of_number(number - 1)
