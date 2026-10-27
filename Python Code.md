## 01. Python Code

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/count-distinct-elements-in-every-window/1)

### Problem Description

**Task:** Given an integer array arr[] and a number k. Find the count of distinct elements in every window of size k in the array.Examples:Input: arr[] = [1, 2, 1, 3, 4, 2, 3], k = 4

#### Examples

##### Example 1

- **Output:**
```text
[1, 1, 1]Explanation: Every window of size 3 in the array [1, 1, 1, 1, 1], contains only the element 1, so the number of distinct elements in each window is 1.
```
- **Explanation:** First window is [1, 2, 1, 3], count of distinct numbers is 3. Second window is [2, 1, 3, 4] count of distinct numbers is 4. Third window is [1, 3, 4, 2] count of distinct numbers is 4. Fourth window is [3, 4, 2, 3] count of distinct numbers is 3.Input: arr[] = [4, 1, 1], k = 2

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(k)

### Accepted Solutions (2)

#### Solution 1 (Python)

- **Submitted:** 2026-10-27 20:41:17
- **Status:** Correct
- **Marks:** 0

```python
from collections import Counter

class Solution:
    def countDistinct(self, arr, k):
        freq = Counter(arr[:k])
        res = [len(freq)]
        for i in range(k, len(arr)):
            left = arr[i - k]
            freq[left] -= 1
            if freq[left] == 0:
                del freq[left]
            freq[arr[i]] += 1
            res.append(len(freq))
        return res
```

#### Solution 2 (Python)

- **Submitted:** 2026-10-24 21:27:58
- **Status:** Correct
- **Marks:** 4

```python
from collections import Counter

class Solution:
    def countDistinct(self, arr, k):
        freq = Counter(arr[:k])
        res = [len(freq)]
        for i in range(k, len(arr)):
            left = arr[i - k]
            freq[left] -= 1
            if freq[left] == 0:
                del freq[left]
            freq[arr[i]] += 1
            res.append(len(freq))
        return res
```

*Generated on: 27/10/2026, 20:41:34*