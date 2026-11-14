## 01. K-th of Two Sorted Arrays

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1)

### Problem Description

**Task:** Given two sorted arrays a[] and b[] and an element k, find the element that would be at the k^th position of the combined sorted array.Examples :Input: a[] = [2, 3, 6, 7, 9], b[] = [1, 4, 8, 10], k = 5

#### Examples

##### Example 1

- **Output:**
```text
6
```
- **Explanation:** The final combined sorted array would be [1, 2, 3, 4, 6, 7, 8, 9, 10]. The 5th element of this array is 6.

##### Example 2

- **Input:**
```text
a[] = [1, 4, 8, 10, 12], b[] = [5, 7, 11, 15, 17], k = 6
```
- **Output:**
```text
10
```
- **Explanation:** Combined sorted array is [1, 4, 5, 7, 8, 10, 11, 12, 15, 17]. The 6th element of this array is 10.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(log(min(a, b)))
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (2)

#### Solution 1 (Python)

- **Submitted:** 2026-11-14 21:53:19
- **Status:** Correct
- **Marks:** 0

```python
import numpy as np

class Solution:
    def kthElement(self, a, b, k):

        arr_a = np.array(a)
        arr_b = np.array(b)

        c = np.concatenate((arr_a, arr_b))
        c.sort()
        return int(c[k - 1])
```

#### Solution 2 (Python)

- **Submitted:** 2026-11-03 18:35:34
- **Status:** Correct
- **Marks:** 4

```python
import numpy as np

class Solution:
    def kthElement(self, a, b, k):

        arr_a = np.array(a)
        arr_b = np.array(b)

        c = np.concatenate((arr_a, arr_b))
        c.sort()
        return int(c[k - 1])
```

*Generated on: 14/11/2026, 21:53:37*