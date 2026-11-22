## 01. Longest Subarray with Sum K

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1)

### Problem Description

**Task:** Given an array arr[] containing integers and an integer k, your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k. If there is no subarray with sum equal to k, return 0.Examples:Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15

#### Examples

##### Example 1

- **Output:**
```text
0
```
- **Explanation:** No subarray with sum = 5 is present in arr[].

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(n)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-11-22 21:03:22
- **Status:** Correct
- **Marks:** 4

```python
class Solution:
    def longestSubarray(self, arr, k):
        seen = {0: -1}
        curr_sum = 0
        best = 0

        for i in range(len(arr)):
            curr_sum += arr[i]

            need = curr_sum - k
            if need in seen:
                length = i - seen[need]
                if length > best:
                    best = length

            if curr_sum not in seen:
                seen[curr_sum] = i

        return best
```

*Generated on: 22/11/2026, 21:03:40*