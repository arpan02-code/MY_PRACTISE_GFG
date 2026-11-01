## 01. Count Set Bits

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/set-bits0143/1)

### Problem Description

**Task:** Given a positive integer n. Return the count of set bits in its binary equivalent.Examples:Input: n = 6

#### Examples

##### Example 1

- **Output:**
```text
2Explanation:Binary representation is '11', so the count of the set bit is 2.
```
- **Explanation:** Binary representation is '1000', so the count of the set bit is 1.Input: n = 3

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(log n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-11-01 22:13:28
- **Status:** Correct
- **Marks:** 2

```python
class Solution:
    def setBits(self, n: int) -> int:
        return bin(n).count('1')
```

*Generated on: 01/11/2026, 22:13:43*