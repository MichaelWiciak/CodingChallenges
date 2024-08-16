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
    """
    To compute the last decimal digit of the expression \( x_1^{x_2^{x_3^{\dots^{x_n}}}} \), you can use modular arithmetic and cyclic properties of last digits. First, determine the cycle length of the last digit for the base number \( x_1 \mod 10 \). Then, reduce the exponent modulo this cycle length to manage the size of the numbers. For nested exponents, compute from the innermost part outward, handling each level with modular reduction based on the cycle of the last digit. Special cases include handling lists with only one element or zeros correctly. By breaking down the problem into these smaller, manageable computations, you avoid direct calculation of excessively large numbers.
    """

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
