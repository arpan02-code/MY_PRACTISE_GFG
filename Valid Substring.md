## 01. Valid Substring

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/valid-substring0624/1)

### Problem Description

**Task:** Given a string s consisting only of opening and closing parentheses '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

> **Note:** The length of the smallest valid substring "()" is 2.

#### Examples

##### Example 1

- **Input:**
```text
s = "(()("
```
- **Output:**
```text
2
```
- **Explanation:** The longest valid substring is "()". Its length is 2.

##### Example 2

- **Input:**
```text
s = "()(())("
```
- **Output:**
```text
6
```
- **Explanation:** The longest valid substring is "()(())". Its length is 6.

##### Example 3

- **Input:**
```text
s = "(()())"
```
- **Output:**
```text
6
```
- **Explanation:** The longest valid substring is "(()())". Its length is 6.

#### Constraints

- **1.** `1 ≤ s.size() ≤ 10⁵s[i] ∈ { '(' , ')' }`

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-10-08 20:26:05
- **Status:** Correct
- **Marks:** 4

```python
class Solution:
    def maxLength(self, s: str) -> int:
        max_len = 0
        left = 0
        right = 0


        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1

            if left == right:
                max_len = max(max_len, 2 * right)
            elif right > left:
                left = 0
                right = 0

        left = 0
        right = 0


        for char in reversed(s):
            if char == '(':
                left += 1
            else:
                right += 1

            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right:
                left = 0
                right = 0

        return max_len
```

*Generated on: 08/10/2026, 20:26:22*