def compress(raw) -> str:
    """
    Compress a list of integers into a string
    :param raw: a list of integers or a string of integers separated by commas
    :return: a string representing the compressed version of the input list
    """

    # If the input is empty, return an empty string
    if not raw:
        return ""

    # if the input is a string, convert it to a list of integers
    if isinstance(raw, str):
        raw = list(map(int, raw.split(",")))

    compressed = []
    n = len(raw)
    i = 0

    # Iterate through the raw list
    while i < n:
        # case 1: identical numbers
        j = i
        # Find the end of the identical numbers
        while j < n and raw[j] == raw[i]:
            j += 1
        # If there are more than 2 identical numbers
        if j - i > 1:
            compressed.append(f"{raw[i]}*{j - i}")
            # Move the pointer to the next number (i=j because j is the number that doesn't match)
            i = j
            continue

        # case 2: consecutive numbers
        j = i
        # Find the end of the consecutive numbers
        while j + 1 < n and raw[j + 1] - raw[j] == raw[i + 1] - raw[i]:
            j += 1
        # If there are more than 2 consecutive numbers
        if j - i >= 2:
            interval = raw[i + 1] - raw[i]
            # If the interval is 1 or -1, don't include the interval
            if interval == 1 or interval == -1:
                compressed.append(f"{raw[i]}-{raw[j]}")
            else:
                compressed.append(f"{raw[i]}-{raw[j]}/{abs(interval)}")
            # Move the pointer to the next number (i=j+1 because j is the last number in the sequence)
            i = j + 1
            continue

        # Single number
        compressed.append(str(raw[i]))
        i += 1

    return ",".join(compressed)


def test():
    TESTS = (
        ("2 identical numbers", [1, 2, 2, 3], "1,2*2,3"),
        ("3 consecutive numbers, ascending", [1, 3, 4, 5, 7], "1,3-5,7"),
        ("3 consecutive numbers, descending", [1, 5, 4, 3, 7], "1,5-3,7"),
        ("3 numbers with same interval, descending", [1, 10, 8, 6, 7], "1,10-6/2,7"),
        ("x", [1, 4, 7, 10, 13, 15, 16, 17, 18, 19, 20, 25], "1-13/3,15-20,25"),
    )

    for name, raw, expected in TESTS:
        result = compress(raw)
        assert result == expected, f"{name}: expected {expected}, but got {result}"
        print(f"{name, raw} -> {result}")

    print("PASSED")


test()
