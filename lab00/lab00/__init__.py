def twenty_twenty_three():
    """Come up with the most creative expression that evaluates to 2023,
    using only numbers and the +, *, and - operators.

    >>> twenty_twenty_three()
    2023
    """
    return 2000 + 30 - 7


def time_to_twenty_twenty_three(year):
    """
    For an integer input from year 0AD to 3000AD, return the difference in years from year "2023"
    """
    if year < 0:
        raise(Exception('The earliest year must be 0!'))
    elif year > 3000:
        raise(Exception('The earliest year must be before 3000!'))
    return abs(2023 - year) 
