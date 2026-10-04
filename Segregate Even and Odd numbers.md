## 01. Segregate Even and Odd numbers

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/segregate-even-and-odd-numbers4629/1)

### Problem Description

**Task:** Given an array arr, write a program segregating even and odd numbers. The program should put all even numbers first in sorted order, and then odd numbers in sorted order.

> **Note:** - You don't need to return the array, you need to modify it in-place.

#### Examples

##### Example 1

- **Input:**
```text
arr[] = [12, 34, 45, 9, 8, 90, 3]
```
- **Output:**
```text
[8, 12, 34, 90, 3, 9, 45]
```
- **Explanation:** Even numbers are 12, 34, 8 and 90. Rest are odd numbers.

##### Example 2

- **Input:**
```text
arr[] = [0, 1, 2, 3, 4]
```
- **Output:**
```text
[0, 2, 4, 1, 3]
```
- **Explanation:** 0 2 4 are even and 1 3 are odd numbers.

##### Example 3

- **Input:**
```text
arr[] = [10, 22, 4, 6]
```
- **Output:**
```text
[4, 6, 10, 22]
```
- **Explanation:** Here all elements are even, so no need of segregataion

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n log n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (3)

#### Solution 1 (Python)

- **Submitted:** 2026-10-04 13:06:18
- **Status:** Correct
- **Marks:** 0

```python
#User function Template for python3
class Solution:
        # code hereclass Solution:
    def segregateEvenOdd(self, arr):
        even = []
        odd = []

        for x in arr:
            if x % 2 == 0:
                even.append(x)
            else:
                odd.append(x)

        even.sort()
        odd.sort()

        arr[:]= even + odd

        return 0

'''class Solution :

    def segregateEvenOdd(arr, n):
        i = -1
        j = 0

        while (j < n):
            if arr[j] % 2 == 0:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
            j += 1


        arr[:i+1] = sorted(arr[:i+1])

        arr[i+1:] = sorted(arr[i+1:])

        return arr'''
```

#### Solution 2 (Python)

- **Submitted:** 2026-10-04 13:06:04
- **Status:** Correct
- **Marks:** 0

```python
#User function Template for python3
class Solution:
        # code hereclass Solution:
    def segregateEvenOdd(self, arr):
        even = []
        odd = []

        for x in arr:
            if x % 2 == 0:
                even.append(x)
            else:
                odd.append(x)

        even.sort()
        odd.sort()

        arr[:]= even + odd

        return 0

'''class Solution :

    def segregateEvenOdd(arr, n):
        i = -1
        j = 0

        while (j < n):
            if arr[j] % 2 == 0:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
            j += 1


        arr[:i+1] = sorted(arr[:i+1])

        arr[i+1:] = sorted(arr[i+1:])

        return arr'''
```

#### Solution 3 (Python)

- **Submitted:** 2026-01-23 12:24:58
- **Status:** Correct
- **Marks:** 1

```python
#User function Template for python3
class Solution:
        # code hereclass Solution:
    def segregateEvenOdd(self, arr):
        even = []
        odd = []

        for x in arr:
            if x % 2 == 0:
                even.append(x)
            else:
                odd.append(x)

        even.sort()
        odd.sort()
        
        arr[:]= even + odd

        return 0

'''class Solution :
    
    def segregateEvenOdd(arr, n):
        i = -1
        j = 0

        while (j < n):
            if arr[j] % 2 == 0:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
            j += 1

    
        arr[:i+1] = sorted(arr[:i+1])
   
        arr[i+1:] = sorted(arr[i+1:])

        return arr'''
```

*Generated on: 04/10/2026, 13:06:37*