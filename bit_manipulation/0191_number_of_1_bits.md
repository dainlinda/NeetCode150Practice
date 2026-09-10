
# Approach

## Check conditions to meet

- input: 
  - n:int / 0 <= n <= 2^31 - 1
- Return the number of 1 bits in its binary representation.

## Key idea

- change it to string form using bin and count '1'

## Complexity
- time: O(logn) for bin, count for O(logn) = O(logn)
  - the number of iterations is equal to a number of bits in the binary representation of a given number n which is log(n) (Siddharth, n.d.)
- space: O(logn) for bin(n)

## Caveat and Reflection (Claude-assisted)

- Another methods(TODO: review later again)
  1. Bit shift loop: Shift n right, check LSB each iteration (`n & 1`), no string allocation. 
    - time O(log n), space O(1).
  2. Hamming weight algorithm (SWAR/bit-trick): Uses bitmasks (e.g. 0x55555555, 0x33333333) to sum bits in parallel across 2-bit, then 4-bit, then 8-bit groups. 
    - time O(1) for fixed-width integers (constant number of operations), space O(1).
  3. Brian Kernighan's: Repeatedly clear the lowest set bit via `n & (n-1)`, count iterations until n == 0. 
    - time O(k) where k = number of 1 bits (worst case O(log n)), space O(1) 
    - only iterates as many times as there are 1s, skipping 0 bits entirely.


## Reference
1. Siddharth. (n.d.). Time complexity of bin() in Python. Stack Overflow. https://stackoverflow.com/questions/50793388/time-complexity-of-bin-in-python