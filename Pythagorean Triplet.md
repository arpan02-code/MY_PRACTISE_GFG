## 01. Pythagorean Triplet

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/pythagorean-triplet3018/1)

### Problem Description

**Task:** Given an array arr[], return true if there is a triplet (a, b, c) from the array (where a, b, and c are on different indexes) that satisfies a^2 + b^2 = c^2, otherwise return false.Examples:Input: arr[] = [3, 2, 4, 6, 5]

#### Examples

##### Example 1

- **Output:**
```text
true
```
- **Explanation:** a = 3, b = 4, and c = 5 forms a pythagorean triplet.

##### Example 2

- **Input:**
```text
arr[] = [3, 8, 5]
```
- **Output:**
```text
false
```
- **Explanation:** No such triplet possible.Input: arr[] = [1, 1, 1]

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n + max(arr[i])^2)
- **Expected Auxiliary Space Complexity:** O(max(arr[i]))

### Accepted Solutions (2)

#### Solution 1 (Python)

- **Submitted:** 2026-11-19 22:30:22
- **Status:** Correct
- **Marks:** 0

```python
class Solution:

  def pythagoreanTriplet(self, arr):
    n = len(arr)
    if n < 3:
      return False

    max_val = max(arr)
    present = [False] * (max_val + 1)
    for x in arr:
      present[x] = True

    # Check pairs (a, b) with a <= b <= max_val
    for a in range(1, max_val + 1):
      if not present[a]:
        continue
      a2 = a * a

      for b in range(a, max_val + 1):
        if not present[b]:
          continue
        c2 = a2 + b * b
        c = int(c2**0.5)

        # Ensure c is an exact integer square root within range
        if c * c == c2 and c <= max_val and present[c]:
          # If a == b, we need at least two occurrences of 'a'
          if a == b and arr.count(a) < 2:
            continue
          return True

    return False
```

#### Solution 2 (Python)

- **Submitted:** 2026-11-19 22:29:20
- **Status:** Correct
- **Marks:** 4

```python
class Solution:

  def pythagoreanTriplet(self, arr):
    n = len(arr)
    if n < 3:
      return False

    max_val = max(arr)
    present = [False] * (max_val + 1)
    for x in arr:
      present[x] = True

    # Check pairs (a, b) with a <= b <= max_val
    for a in range(1, max_val + 1):
      if not present[a]:
        continue
      a2 = a * a

      for b in range(a, max_val + 1):
        if not present[b]:
          continue
        c2 = a2 + b * b
        c = int(c2**0.5)

        # Ensure c is an exact integer square root within range
        if c * c == c2 and c <= max_val and present[c]:
          # If a == b, we need at least two occurrences of 'a'
          if a == b and arr.count(a) < 2:
            continue
          return True

    return False
```

*Generated on: 19/11/2026, 22:30:44*