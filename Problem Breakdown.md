## 01. Problem Breakdown

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1)

### Problem Description

**Task:** Given a string s, reverse the string without reversing its individual words. Words are separated by dots(.).The string may contain leading or trailing dots(.) or multiple dots(.) between two words. The returned string should only have a single dot(.) separating the words and no extra dots should be included.Examples :Input: s = "i.like.this.program.very.much"Output: "much.very.program.this.like.i"

#### Examples

##### Example 1

- **Output:**
```text
"home"
```
- **Explanation:** The input string contains only one word with extra dots around it. After removing the extra dots, the output is "home".

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (5)

#### Solution 1 (Python)

- **Submitted:** 2026-11-14 21:50:08
- **Status:** Correct
- **Marks:** 0

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return '.'.join([w for w in s.split('.') if w][::-1])
```

#### Solution 2 (Python)

- **Submitted:** 2026-11-08 16:50:44
- **Status:** Correct
- **Marks:** 0

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return '.'.join([w for w in s.split('.') if w][::-1])
```

#### Solution 3 (Python)

- **Submitted:** 2026-11-08 16:28:24
- **Status:** Correct
- **Marks:** 0

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return '.'.join([w for w in s.split('.') if w][::-1])
```

#### Solution 4 (Python)

- **Submitted:** 2026-11-08 16:26:21
- **Status:** Correct
- **Marks:** 0

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return '.'.join([w for w in s.split('.') if w][::-1])
```

#### Solution 5 (Python)

- **Submitted:** 2026-11-08 16:25:56
- **Status:** Correct
- **Marks:** 2

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return '.'.join([w for w in s.split('.') if w][::-1])
```

*Generated on: 14/11/2026, 21:50:32*