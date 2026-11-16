## 01. Minimize the Heights

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/minimize-the-heights3351/1)

### Problem Description

**Task:** Given an array arr[] representing the heights of n towers and a positive integer k. For each tower, perform exactly one of the following operations exactly once:Increase its height by k, orDecrease its height by k.After performing the operation on every tower, the height of any tower must not become negative.Return the minimum possible difference between the heights of the tallest and the shortest towers after modifying all the towers.Examples :Input: k = 2, arr[] = [1, 5, 8, 10]

#### Examples

##### Example 1

- **Output:**
```text
5
```
- **Explanation:** The array can be modified as [1+k, 5-k, 8-k, 10-k] = [3, 3, 6, 8]. The difference between the largest and the smallest is 8-3 = 5.

##### Example 2

- **Input:**
```text
k = 3, arr[] = [3, 9, 12, 16, 20]
```
- **Output:**
```text
11
```
- **Explanation:** The array can be modified as [3+k, 9+k, 12-k, 16-k, 20-k] = [6, 12, 9, 13, 17]. The difference between the largest and the smallest is 17-6 = 11.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n log n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-11-16 21:21:39
- **Status:** Correct
- **Marks:** 4

```python
class Solution:
    def getMinDiff(self, arr, k):
        arr.sort()
        n = len(arr)
        ans = arr[-1] - arr[0]

        for i in range(1, n):
            if arr[i] - k < 0:
                continue

            min_h = min(arr[0] + k, arr[i] - k)
            max_h = max(arr[i - 1] + k, arr[-1] - k)

            ans = min(ans, max_h - min_h)

        return ans
```

*Generated on: 16/11/2026, 21:21:58*