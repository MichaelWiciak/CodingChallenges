def next_smaller(n):
    return -1


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
