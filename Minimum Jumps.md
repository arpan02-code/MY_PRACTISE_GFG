## 01. Minimum Jumps

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1)

### Problem Description

**Task:** Given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position.
For example:
If arr[i] = 3, you can jump to index i + 1, i + 2, or i + 3 from position i.
If arr[i] = 0, you cannot jump forward from that position.
Find the minimum number of jumps needed to move from the first position in the array to the last position.

> **Note:** Return -1 if you can't reach the end of the array.

#### Examples

##### Example 1

- **Input:**
```text
arr[] = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
```
- **Output:**
```text
3
```
- **Explanation:** First jump from 1st element to 2nd element with value 3. From here we jump to 5th element with value 9, and from here we will jump to the last.

##### Example 2

- **Input:**
```text
arr = [1, 4, 3, 2, 6, 7]Output: 2
```
- **Explanation:** First we jump from the 1st to 2nd element and then jump to the last element.

##### Example 3

- **Input:**
```text
arr = [0, 10, 20]Output: -1
```
- **Explanation:** We cannot go anywhere from the 1st element.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-11-23 22:38:24
- **Status:** Correct
- **Marks:** 4

```python
class Solution:

  def minJumps(self, arr: list[int]) -> int:
    n = len(arr)
    if n <= 1:
      return 0
    if arr[0] == 0:
      return -1

    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n - 1):
      farthest = max(farthest, i + arr[i])

      if farthest <= i:
        return -1

      if i == current_end:
        jumps += 1
        current_end = farthest
        if current_end >= n - 1:
          break

    return jumps if current_end >= n - 1 else -1
```

*Generated on: 23/11/2026, 22:38:44*