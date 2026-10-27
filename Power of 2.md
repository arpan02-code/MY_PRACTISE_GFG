## 01. Power of 2

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/power-of-2-1587115620/1)

### Problem Description

**Task:** Given a non-negative integer n, return true if it is a power of 2. Otherwise, return false. Examples:Input: n = 8

#### Examples

##### Example 1

- **Output:**
```text
true
```
- **Explanation:** 1 is equal to 2 raised to 0 (2⁰ = 1).

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(1)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (2)

#### Solution 1 (Python)

- **Submitted:** 2026-10-27 20:38:01
- **Status:** Correct
- **Marks:** 0

```python
class Solution:
    def isPowerofTwo(self, n):
        # code here
        return n> 0 and (n&(n-1))==0
```

#### Solution 2 (Python)

- **Submitted:** 2026-10-27 19:51:03
- **Status:** Correct
- **Marks:** 2

```python
class Solution:
    def isPowerofTwo(self, n):
        # code here
        return n> 0 and (n&(n-1))==0
```

*Generated on: 27/10/2026, 20:38:17*