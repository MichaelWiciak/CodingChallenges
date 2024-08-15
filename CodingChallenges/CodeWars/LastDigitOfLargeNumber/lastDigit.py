def last_digit(lst):
    if not lst:
        return 1

    # Start from the end of the list and work backwards
    exp = 1  # The effective exponent
    for num in reversed(lst[1:]):  # Exclude the first number
        if exp > 4:  # By modular arithmetic, only powers of 4 matter for last digits
            exp = exp % 4 + 4
        exp = pow(num, exp, 4)

    # Compute the last digit of the base raised to the effective exponent
    return pow(lst[0], exp, 10)
