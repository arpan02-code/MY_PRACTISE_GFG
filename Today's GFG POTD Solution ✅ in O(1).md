## 01. Today's GFG POTD Solution ✅ in O(1)

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/reverse-coding2452/1)

### Problem Description

**Task:** Given an integer n, compute the sum of all natural numbers from 1 to n (inclusive). If n is 0, the sum should be 0.Examples:Input: n = 6

#### Examples

##### Example 1

- **Output:**
```text
0
```
- **Explanation:** Since n is 0, the sum is 0.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(1)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-11-26 21:36:55
- **Status:** Correct
- **Marks:** 1

```python
def solve(n):
  total = 0
  for x in range(1, n + 1):
    total += x
  return total


n = int(input())
print(solve(n))
```

*Generated on: 26/11/2026, 21:37:16*