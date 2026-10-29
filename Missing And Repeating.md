## 01. Missing And Repeating

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/1)

### Problem Description

**Task:** Given an unsorted array arr[] of size n, containing elements from the range 1 to n, it is known that one number in this range is missing, and another number occurs twice in the array, find the both numbers.Examples:Input: arr[] = [2, 2]

#### Examples

##### Example 1

- **Output:**
```text
[3, 2]
```
- **Explanation:** Repeating number is 3 and the missing number is 2.Input: arr[] = [4, 3, 6, 2, 1, 1]Output: [1, 5]Explanation: Repeating number is 1 and the missing number is 5.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-10-29 21:46:32
- **Status:** Correct
- **Marks:** 2

```python
class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        s = set(arr)
        a = sum(arr) - sum(s)
        b = n * (n + 1) // 2 - sum(s)
        return [a, b]
```

*Generated on: 29/10/2026, 21:46:37*