## 01. Largest in Array

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/largest-element-in-array4009/1)

### Problem Description

**Task:** Given an array arr[]. The task is to find the largest element and return it.Examples:Input: arr[] = [1, 8, 7, 56, 90]

#### Examples

##### Example 1

- **Output:**
```text
10
```
- **Explanation:** There is only one element which is the largest.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (3)

#### Solution 1 (Python)

- **Submitted:** 2026-10-04 13:01:59
- **Status:** Correct
- **Marks:** 0

```python
class Solution:
    def largest(self, arr):
        largest = arr[0]

        for i in arr:
            if largest < i:
                largest  = i
        return largest
```

#### Solution 2 (Python)

- **Submitted:** 2026-10-04 13:01:06
- **Status:** Correct
- **Marks:** 0

```python
class Solution:
    def largest(self, arr):
        largest = arr[0]

        for i in arr:
            if largest < i:
                largest  = i
        return largest
```

#### Solution 3 (Python)

- **Submitted:** 2026-01-22 10:35:15
- **Status:** Correct
- **Marks:** 1

```python
class Solution:
    def largest(self, arr):
        largest = arr[0]
        
        for i in arr:
            if largest < i:
                largest  = i
        return largest
```

*Generated on: 04/10/2026, 13:02:17*