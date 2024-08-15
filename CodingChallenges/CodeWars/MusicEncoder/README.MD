# Signal Compression

## Specification

The task is to compress an input signal represented as an array of integers by identifying and shortening regularities in the sequence.

### Compression Rules

1. **Identical Numbers**: A sequence of 2 or more identical numbers is shortened as `number*count`.
2. **Consecutive Numbers**: A sequence of 3 or more consecutive numbers is shortened as `first-last`. This applies to both ascending and descending orders.
3. **Equal Interval Numbers**: A sequence of 3 or more numbers with the same interval is shortened as `first-last/interval`. Note that the interval does **not** need a sign.
4. **Order of Compression**: Compression is performed from left to right.

### Examples

- Input: `[1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]`  
  Output: `"1,3-5,7-11,14,15,17-20"`

- Input: `[0, 2, 4, 5, 7, 8, 9]`  
  Output: `"0-4/2,5,7-9"`

- Input: `[0, 2, 4, 5, 7, 6, 5]`  
  Output: `"0-4/2,5,7-5"`

- Input: `[0, 2, 4, 5, 7, 6, 5, 5, 5, 5, 5]`  
  Output: `"0-4/2,5,7-5,5*4"`

- Input: `'1,5,4,3,7'`  
  Output: `'1,5-3,7'`

- Input: `'1,10,8,6,7'`  
  Output: `'1,10-6/2
