## 01. Checking K-th Bit

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/check-whether-k-th-bit-is-set-or-not-1587115620/1)

### Problem Description

**Task:** Given two positive integer n and k, check if the k^th index bit of n is set or not. A bit is called set if it is 1. Examples : Input: n = 4, k = 0

#### Examples

##### Example 1

- **Output:**
```text
true
```
- **Explanation:** Binary representation of 4 is 100, in which 2^nd index bit from LSB is set. So, return true.Input: n = 500, k = 3Output: falseExplanation: Binary representation of 500 is 111110100, in which 3rd index bit from LSB is not set. So, return false.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(1)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-10-28 20:36:47
- **Status:** Correct
- **Marks:** 2

```python
class Solution:
    def checkKthBit(self, n, k):
        return (n >> k) & 1 == 1
```

*Generated on: 28/10/2026, 20:36:55*