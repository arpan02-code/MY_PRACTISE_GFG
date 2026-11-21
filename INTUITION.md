## 01. INTUITION

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/rearrange-an-array-with-o1-extra-space3142/1)

### Problem Description

**Task:** Given an integer array arr[] of size n, where each element lies in the range [0, n-1], transform the array such that every element at index i becomes:arr[i] = arr[arr[i]].The transformation must be performed in-place, meaning the same array should store both the original and updated values without using another array.Examples:Input: arr[] = [1, 0]

#### Examples

##### Example 1

- **Output:**
```text
[0, 1]
```
- **Explanation:** The original array is [1, 0]. At index 0, arr[0] = 1, so the new value becomes arr[1] = 0. At index 1, arr[1] = 0, so the new value becomes arr[0] = 1. Thus, the transformed array becomes [0, 1].

##### Example 2

- **Input:**
```text
arr[] = [4, 0, 2, 1, 3]
```
- **Output:**
```text
[3, 4, 2, 0, 1]
```
- **Explanation:** The original array is [4, 0, 2, 1, 3]. Each element is replaced by the value at index arr[i] in the original array. So the new values become 3, 4, 2, 0, 1 respectively, and the transformed array becomes [3, 4, 2, 0, 1].

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (2)

#### Solution 1 (Python)

- **Submitted:** 2026-11-21 23:02:19
- **Status:** Correct
- **Marks:** 0

```python
class Solution:

  def arrange(self, arr):
    n = len(arr)

    # Step 1: Store both old and new values in arr[i]
    for i in range(n):
      old_val_at_target = arr[arr[i]] % n
      arr[i] += old_val_at_target * n

    # Step 2: Extract the final transformed values
    for i in range(n):
        
      arr[i] //= n

    return arr
```

#### Solution 2 (Python)

- **Submitted:** 2026-11-21 23:01:24
- **Status:** Correct
- **Marks:** 4

```python
class Solution:

  def arrange(self, arr):
    n = len(arr)

    # Step 1: Store both old and new values in arr[i]
    for i in range(n):
      old_val_at_target = arr[arr[i]] % n
      arr[i] += old_val_at_target * n

    # Step 2: Extract the final transformed values
    for i in range(n):
        
      arr[i] //= n

    return arr
```

*Generated on: 21/11/2026, 23:02:39*