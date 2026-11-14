## 01. Two odd Occuring

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/two-numbers-with-odd-occurrences5846/1)

### Problem Description

**Task:** Given an unsorted array, arr[] of positive numbers that contains even number of occurrences for all numbers except two numbers. Return that two numbers in decreasing order which has odd occurrences.Examples:

#### Examples

##### Example 1

- **Input:**
```text
arr = [4, 2, 4, 5, 2, 3, 3, 1]
```
- **Output:**
```text
[5, 1]
```
- **Explanation:** 5 and 1 have odd occurrences.

##### Example 2

- **Input:**
```text
arr[] = [1, 7, 5, 7, 5, 4, 7, 4]
```
- **Output:**
```text
[7, 1]
```
- **Explanation:** 7 and 1 have odd occurrences.

#### Constraints

- **1.** `2 ≤ arr.size() ≤ 10⁶¹ ≤ arr[i]≤ 10⁷`

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (3)

#### Solution 1 (Python)

- **Submitted:** 2026-11-14 21:43:36
- **Status:** Correct
- **Marks:** 0

```python
class Solution:

  def twoOddNum(self, arr):
    # Step 1: XOR all elements in the array
    xor_sum = 0
    for num in arr:
      xor_sum ^= num

    # Step 2: Find the rightmost set bit
    rightmost_bit = xor_sum & -xor_sum

    # Step 3: Divide elements into two groups and XOR them separately
    num1 = 0
    num2 = 0
    for num in arr:
      if num & rightmost_bit:
        num1 ^= num
      else:
        num2 ^= num

    # Step 4: Return both numbers in decreasing order
    return [num1, num2] if num1 > num2 else [num2, num1]
```

#### Solution 2 (Python)

- **Submitted:** 2026-11-14 21:25:14
- **Status:** Correct
- **Marks:** 0

```python
class Solution:

  def twoOddNum(self, arr):
    # Step 1: XOR all elements in the array
    xor_sum = 0
    for num in arr:
      xor_sum ^= num

    # Step 2: Find the rightmost set bit
    rightmost_bit = xor_sum & -xor_sum

    # Step 3: Divide elements into two groups and XOR them separately
    num1 = 0
    num2 = 0
    for num in arr:
      if num & rightmost_bit:
        num1 ^= num
      else:
        num2 ^= num

    # Step 4: Return both numbers in decreasing order
    return [num1, num2] if num1 > num2 else [num2, num1]
```

#### Solution 3 (Python)

- **Submitted:** 2026-11-14 21:21:31
- **Status:** Correct
- **Marks:** 4

```python
class Solution:

  def twoOddNum(self, arr):
    # Step 1: XOR all elements in the array
    xor_sum = 0
    for num in arr:
      xor_sum ^= num

    # Step 2: Find the rightmost set bit
    rightmost_bit = xor_sum & -xor_sum

    # Step 3: Divide elements into two groups and XOR them separately
    num1 = 0
    num2 = 0
    for num in arr:
      if num & rightmost_bit:
        num1 ^= num
      else:
        num2 ^= num

    # Step 4: Return both numbers in decreasing order
    return [num1, num2] if num1 > num2 else [num2, num1]
```

*Generated on: 14/11/2026, 21:43:53*