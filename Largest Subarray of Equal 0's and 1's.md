## 01. Largest Subarray of Equal 0's and 1's

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/largest-subarray-of-0s-and-1s/1)

### Problem Description

**Task:** Given an array arr of 0s and 1s. Find and return the length of the longest subarray with equal number of 0s and 1s.Examples:Input: arr[] = [1, 0, 1, 1, 1, 0, 0]

#### Examples

##### Example 1

- **Output:**
```text
0Explanation: There is no subarray with an equal number of 0s and 1s.
```
- **Explanation:** arr[1...6] is the longest subarray with three 0s and three 1s.Input: arr[] = [0, 0, 1, 1, 0]

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(n)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-10-20 07:05:08
- **Status:** Correct
- **Marks:** 4

```python
class Solution:
    def maxLen(self, arr):
        hash_map = {}
        max_len = 0
        curr_sum = 0
        for i in range(len(arr)):
            curr_sum += -1 if arr[i] == 0 else 1
            if curr_sum == 0:
                max_len = i + 1
            if curr_sum in hash_map:
                max_len = max(max_len, i - hash_map[curr_sum])
            else:
                hash_map[curr_sum] = i
        return max_len
```

*Generated on: 20/10/2026, 07:05:23*