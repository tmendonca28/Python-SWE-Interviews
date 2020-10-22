"""
Write a function that takes in an int year and
returns True or False depending on if the year is
a leap year.
"""

def is_leap_year(year : int) -> bool:
    if year<1:
        return False
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 ==0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return False