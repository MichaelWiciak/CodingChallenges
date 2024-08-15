# Last Digit of a Large Exponentiation

## Description

Given a list `[x1, x2, x3, ..., xn]`, the task is to compute the last (decimal) digit of the expression:

\[ x_1 ^ {x_2 ^ {x_3 ^ { \cdots ^ {x_n} }}} \]

### Example

For example, with the input `[3, 4, 2]`, your code should return `1` because:

\[ 3 ^ {(4 ^ 2)} = 3 ^ {16} = 43046721 \]

The last digit is `1`.

### Important Notes

- **Rapid Growth**: Powers grow incredibly fast. For instance, \( 9 ^ {9 ^ 9} \) has more than 369 million digits. The solution must efficiently handle such large numbers.
- **Corner Cases**:
  - We assume that \( 0 ^ 0 = 1 \).
  - The last digit of an empty list equals `1`.

### Test Cases

Here are some test cases to illustrate the expected behavior:

- `([], 1)`
- `([0, 0], 1)`
- `([0, 0, 0], 0)`
- `([1, 2], 1)`
- `([3, 4, 5], 1)`
- `([4, 3, 6], 4)`
- `([7, 6, 21], 1)`
- `([12, 30, 21], 6)`
- `([2, 2, 2, 0], 4)`
- `([937640, 767456, 981242], 0)`
- `([123232, 694022, 140249], 6)`
- `([499942, 898102, 846073], 6)`

---

## License

This project is licensed under the MIT License.
