## 01. Alternate Positive Negative

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/array-of-alternate-ve-and-ve-nos1401/1)

### Problem Description

**Task:** Given an unsorted array arr containing both positive and negative numbers. Your task is to rearrange the array and convert it into an array of alternate positive and negative numbers without changing the relative order.Note: Resulting array should start with a positive integer (0 will also be considered as a positive integer). If any of the positive or negative integers are exhausted, then add the remaining integers in the answer as it is by maintaining the relative order.Examples:Input: arr[] = [9, 4, -2, -1, 5, 0, -5, -3, 2]

#### Examples

##### Example 1

- **Output:**
```text
[9, -2, 4, -1, 5, -5, 0, -3, 2]
```
- **Explanation:** The positive numbers are [9, 4, 5, 0, 2] and the negative integers are [-2, -1, -5, -3]. Since, we need to start with the positive integer first and then negative integer and so on (by maintaining the relative order as well), hence we will take 9 from the positive set of elements and then -2 after that 4 and then -1 and so on.

##### Example 2

- **Input:**
```text
arr[] = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
```
- **Output:**
```text
[9, -2, 5, -1, 5, -5, 0, -3, 2]
```
- **Explanation:** The positive numbers are [9, 5, 5, 0, 2] and the negative integers are [-2, -1, -5, -3]. Since, we need to start with the positive integer first and then negative integer and so on (by maintaining the relative order as well), hence we will take 9 from the positive set of elements and then -2 after that 5 and then -1 and so on.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(n)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-10-19 17:54:28
- **Status:** Correct
- **Marks:** 2

```python
class Solution:
    def rearrange(self, arr):
        pos = [x for x in arr if x >= 0]
        neg = [x for x in arr if x < 0]

        i = j = k = 0
        while i < len(pos) and j < len(neg):
            if k % 2 == 0:
                arr[k] = pos[i]
                i += 1
            else:
                arr[k] = neg[j]
                j += 1
            k += 1

        while i < len(pos):
            arr[k] = pos[i]
            i += 1
            k += 1

        while j < len(neg):
            arr[k] = neg[j]
            j += 1
            k += 1
```

*Generated on: 19/10/2026, 17:54:39*