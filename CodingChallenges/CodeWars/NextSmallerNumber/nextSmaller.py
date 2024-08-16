def next_smaller(n):
    return -1


def next_smaller_naive(n) -> int:
    """Naive Permutation Approach
    Generate all permutations of the digits of the number, sort them, and find the largest one that is smaller than the original number.
    Computationally expensive, so this approach is best for smaller cases. Note that numbers that contain 0's cannot start with 0.

    Noe that this approach failed for tests with large numbers.
    """

    from itertools import permutations

    n_str = str(n)
    n_digits = len(n_str)

    # Generate permutations of the digits of n
    n_permutations = list(permutations(n_str, n_digits))

    # Convert each permutation to an integer and filter out those starting with '0'
    n_permutations = sorted(
        [int("".join(perm)) for perm in n_permutations if perm[0] != "0"]
    )

    # Filter out permutations that are not less than n
    n_permutations = [perm for perm in n_permutations if perm < n]

    # Return the largest permutation that is less than n, or -1 if none exist
    return n_permutations[-1] if n_permutations else -1


def next_smaller_backwards(n) -> int:
    """Reverse Engineering the Next Smaller Number
    Start from the rightmost digits and move leftwards to find the first digit that can be swapped to form a smaller number.
    You want to find the first digit that is larger than the digit to its right. This is the point where you can swap to get a smaller number.
    After identifying this point, swap the identified digit with the largest possible smaller digit on its right side, and then sort the remaining digits in descending order to get the largest possible number smaller than the original.
    """

    n_str = str(n)
    n_digits = len(n_str)

    # Find the first digit that is larger than the digit to its right
    for i in range(n_digits - 1, 0, -1):
        if n_str[i] < n_str[i - 1]:
            break
    else:
        # No such digit found, no smaller number possible
        return -1

    # Identify the digit to swap
    swap_index = i - 1
    swap_digit = n_str[swap_index]

    # Find the largest possible digit to the right of the identified digit that is smaller than it
    swap_with_index = -1
    for j in range(n_digits - 1, swap_index, -1):
        if n_str[j] < swap_digit:
            if swap_with_index == -1 or n_str[j] > n_str[swap_with_index]:
                swap_with_index = j

    if swap_with_index == -1:
        # No valid swap can make the number smaller
        return -1

    # Swap the digits
    n_list = list(n_str)
    n_list[swap_index], n_list[swap_with_index] = (
        n_list[swap_with_index],
        n_list[swap_index],
    )

    # Sort the remaining digits to the right of the swap index in descending order
    n_list = n_list[: swap_index + 1] + sorted(n_list[swap_index + 1 :], reverse=True)

    # Convert list back to integer and handle leading zeros

    result = int("".join(n_list))
    if result >= n:
        return -1  # If the result is not smaller, return -1
    if n_list[0] == "0":  # Leading zero case
        return -1

    return result


def assertEquals(var1, var2):
    if var1 == var2:
        print("Assertion passed for: ", var1)
        return True
    else:
        print(f"Assertion failed: {var1} != {var2}")
        return False


def example_cases():
    assertEquals(next_smaller(907), 790)
    assertEquals(next_smaller(531), 513)
    assertEquals(next_smaller(135), -1)
    assertEquals(next_smaller(2071), 2017)
    assertEquals(next_smaller(414), 144)
    assertEquals(next_smaller(123456798), 123456789)
    assertEquals(next_smaller(123456789), -1)
    assertEquals(next_smaller(1234567908), 1234567890)


example_cases()
