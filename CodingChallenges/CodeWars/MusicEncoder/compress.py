def compress(raw):

    if not raw:
        return ""

    compressed = []
    n = len(raw)
    i = 0

    # Iterate through the raw list
    while i < n:
        # Identical numbers
        j = i
        # Find the end of the identical numbers
        while j < n and raw[j] == raw[i]:
            j += 1
        if j - i > 1:
            compressed.append(f"{raw[i]}*{j - i}")
            i = j
            continue

        # Consecutive numbers (ascending or descending)
        j = i
        while j + 1 < n and raw[j + 1] - raw[j] == raw[i + 1] - raw[i]:
            j += 1
        if j - i >= 2:
            interval = raw[i + 1] - raw[i]
            if interval == 1 or interval == -1:
                compressed.append(f"{raw[i]}-{raw[j]}")
            else:
                compressed.append(f"{raw[i]}-{raw[j]}/{abs(interval)}")
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
    )

    for name, raw, expected in TESTS:
        result = compress(raw)
        assert result == expected, f"{name}: expected {expected}, but got {result}"
        print(f"{name, raw} -> {result}")

    print("PASSED")


test()
