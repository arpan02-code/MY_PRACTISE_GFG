## 01. Problem: MultiplyStrings

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/multiply-two-strings/1)

### Problem Description

**Task:** Given two numbers as strings s1 and s2. Calculate their Product.Note: The numbers can be negative and You are not allowed to use any built-in function or convert the strings to integers. There can be zeros in the begining of the numbers. You don't need to specify '+' sign in the begining of positive numbers.Examples:Input: s1 = "0033", s2 = "2"

#### Examples

##### Example 1

- **Output:**
```text
"0"Explanation: Anything multiplied by 0 is equal to 0.
```

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n * m)
- **Expected Auxiliary Space Complexity:** O(n + m)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-11-28 08:36:21
- **Status:** Correct
- **Marks:** 4

```python
class Solution:
    def multiplyStrings(self, s1, s2):
        neg = False
        if s1 and s1[0] == "-":
            neg = not neg
            s1 = s1[1:]
        elif s1 and s1[0] == "+":
            s1 = s1[1:]

        if s2 and s2[0] == "-":
            neg = not neg
            s2 = s2[1:]
        elif s2 and s2[0] == "+":
            s2 = s2[1:]

        m, n = len(s1), len(s2)
        if m == 0 or n == 0:
            return "0"

        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            d1 = ord(s1[i]) - ord("0")
            for j in range(n - 1, -1, -1):
                d2 = ord(s2[j]) - ord("0")
                total = d1 * d2 + res[i + j + 1]
                res[i + j + 1] = total % 10
                res[i + j] += total // 10

        idx = 0
        while idx < len(res) and res[idx] == 0:
            idx += 1

        if idx == len(res):
            return "0"

        digits = "".join(str(x) for x in res[idx:])
        if neg:
            return "-" + digits
        return digits
```

*Generated on: 28/11/2026, 08:36:37*