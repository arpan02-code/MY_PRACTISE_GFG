## 01. Implement Atoi

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/implement-atoi/1)

### Problem Description

**Task:** Given a string s, convert it into a 32-bit signed integer (similar to the atoi() function) without using any built-in conversion functions.The conversion follows these rules:Ignore Leading Whitespaces: Skip all leading whitespace characters.Check Sign: If the next character is either '+' or '-', take it as the sign of the number. If no sign is present, assume the number is positive.Read Digits: Read the digits and ignore any leading zeros. Stop reading when a non-digit character is encountered or the end of the string is reached. If no digits are found, return 0.Handle Overflow: If the number exceeds the range of a 32-bit signed integer:Return 2³¹ − 1 (i.e., 2147483647) if it is greater than the maximum value.Return −2³¹ (i.e., -2147483648) if it is smaller than the minimum value.Return the final integer value.Examples:Input: s = "-123"

#### Examples

##### Example 1

- **Output:**
```text
2147483647Explanation: The converted number will be greater than 2³¹ – 1, therefore print 2³¹ – 1 = 2147483647.
```

##### Example 2

- **Input:**
```text
s = "-999999999999"
```
- **Output:**
```text
-12
```
- **Explanation:** Nothing is read after -12 as a non-digit character ‘g’ was encountered.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (2)

#### Solution 1 (Python)

- **Submitted:** 2026-11-25 22:14:54
- **Status:** Correct
- **Marks:** 0

```python
class Solution:

    def myAtoi(self, s):
        n = len(s)
        i = 0

        while i < n and s[i] == " ":
            i += 1

        sign = 1
        if i < n and (s[i] == "+" or s[i] == "-"):
            if s[i] == "-":
                sign = -1
            i += 1

        num = 0
        while i < n and "0" <= s[i] <= "9":
            digit = ord(s[i]) - ord("0")
            num = num * 10 + digit
            i += 1

        result = sign * num
        min_int = -(2**31)
        max_int = 2**31 - 1

        if result < min_int:
            return min_int
        if result > max_int:
            return max_int
        return result
```

#### Solution 2 (Python)

- **Submitted:** 2026-11-25 22:14:42
- **Status:** Correct
- **Marks:** 4

```python
class Solution:

    def myAtoi(self, s):
        n = len(s)
        i = 0

        while i < n and s[i] == " ":
            i += 1

        sign = 1
        if i < n and (s[i] == "+" or s[i] == "-"):
            if s[i] == "-":
                sign = -1
            i += 1

        num = 0
        while i < n and "0" <= s[i] <= "9":
            digit = ord(s[i]) - ord("0")
            num = num * 10 + digit
            i += 1

        result = sign * num
        min_int = -(2**31)
        max_int = 2**31 - 1

        if result < min_int:
            return min_int
        if result > max_int:
            return max_int
        return result
```

*Generated on: 25/11/2026, 22:15:14*