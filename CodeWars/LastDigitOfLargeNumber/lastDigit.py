def last_digit(lst):
    pass


def last_digit_naive(lst):
    """
    Naive approach: take the last number and raise it to the power of the next number until you reach the first number.
    """

    if not lst:
        return 1

    result = 1
    for i in range(len(lst) - 1, -1, -1):
        result = lst[i] ** (result if i == len(lst) - 1 else result % 4 + 4)
    return result % 10


def last_digit_simplified(lst):

    if not lst:
        return 1

    def cycle_length(n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 4
        if n == 3:
            return 4
        if n == 4:
            return 2
        if n == 5:
            return 1
        if n == 6:
            return 1
        if n == 7:
            return 4
        if n == 8:
            return 4
        if n == 9:
            return 2

    result = 1
    for i in range(len(lst) - 1, -1, -1):
        result = lst[i] ** (
            result
            if i == len(lst) - 1
            else result % cycle_length(lst[i]) + cycle_length(lst[i])
        )
    return result % 10
