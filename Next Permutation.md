## 01. Next Permutation

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/next-permutation5226/1)

### Problem Description

**Task:** Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers into the lexicographically smallest greater (or next) permutation. If no next permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order). Examples:Input: arr[] = [2, 4, 1, 7, 5, 0]

#### Examples

##### Example 1

- **Output:**
```text
[3, 4, 5, 1, 2]
```
- **Explanation:** The next permutation of the given array is [3, 4, 5, 1, 2].

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-11-20 22:35:22
- **Status:** Correct
- **Marks:** 4

```python
class Solution:

  def nextPermutation(self, arr):
    n = len(arr)

    pivot = -1
    for i in range(n - 2, -1, -1):
      if arr[i] < arr[i + 1]:
        pivot = i
        break

    if pivot == -1:
      arr.reverse()
      return

    for j in range(n - 1, pivot, -1):
      if arr[j] > arr[pivot]:
        arr[pivot], arr[j] = arr[j], arr[pivot]
        break

    left, right = pivot + 1, n - 1
    while left < right:
      arr[left], arr[right] = arr[right], arr[left]
      left += 1
      right -= 1
```

*Generated on: 20/11/2026, 22:35:27*