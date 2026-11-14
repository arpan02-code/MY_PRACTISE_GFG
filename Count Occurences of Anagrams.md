## 01. Count Occurences of Anagrams

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1)

### Problem Description

**Task:** Given a word pat and a text txt. Return the count of the occurrences of anagrams of the word in the text.Example 1:Input: txt = "forxxorfxdofr", pat = "for"

#### Examples

##### Example 1

- **Output:**
```text
3
```
- **Explanation:** for, orf and ofr appears in the txt, hence answer is 3.

##### Example 2

- **Input:**
```text
txt = "aabaabaa", pat = "aaba"
```
- **Output:**
```text
4
```
- **Explanation:** aaba is present 4 times in txt.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (4)

#### Solution 1 (Python)

- **Submitted:** 2026-11-14 21:44:47
- **Status:** Correct
- **Marks:** 0

```python
from collections import Counter


class Solution:

  def search(self, pat, txt):
    k = len(pat)
    n = len(txt)
    if k > n:
      return 0

    pat_count = Counter(pat)
    window_count = Counter(txt[:k])

    ans = 0
    if pat_count == window_count:
      ans += 1

    for i in range(k, n):
      # Add the next character in the window
      window_count[txt[i]] += 1

      # Remove the first character of the previous window
      old_char = txt[i - k]
      window_count[old_char] -= 1
      if window_count[old_char] == 0:
        del window_count[old_char]

      # Compare window frequency with pattern frequency
      if pat_count == window_count:
        ans += 1

    return ans
```

#### Solution 2 (Python)

- **Submitted:** 2026-11-13 20:10:05
- **Status:** Correct
- **Marks:** 0

```python
from collections import Counter


class Solution:

  def search(self, pat, txt):
    k = len(pat)
    n = len(txt)
    if k > n:
      return 0

    pat_count = Counter(pat)
    window_count = Counter(txt[:k])

    ans = 0
    if pat_count == window_count:
      ans += 1

    for i in range(k, n):
      # Add the next character in the window
      window_count[txt[i]] += 1

      # Remove the first character of the previous window
      old_char = txt[i - k]
      window_count[old_char] -= 1
      if window_count[old_char] == 0:
        del window_count[old_char]

      # Compare window frequency with pattern frequency
      if pat_count == window_count:
        ans += 1

    return ans
```

#### Solution 3 (Python)

- **Submitted:** 2026-11-13 20:09:23
- **Status:** Correct
- **Marks:** 0

```python
from collections import Counter


class Solution:

  def search(self, pat, txt):
    k = len(pat)
    n = len(txt)
    if k > n:
      return 0

    pat_count = Counter(pat)
    window_count = Counter(txt[:k])

    ans = 0
    if pat_count == window_count:
      ans += 1

    for i in range(k, n):
      # Add the next character in the window
      window_count[txt[i]] += 1

      # Remove the first character of the previous window
      old_char = txt[i - k]
      window_count[old_char] -= 1
      if window_count[old_char] == 0:
        del window_count[old_char]

      # Compare window frequency with pattern frequency
      if pat_count == window_count:
        ans += 1

    return ans
```

#### Solution 4 (Python)

- **Submitted:** 2026-11-13 20:08:57
- **Status:** Correct
- **Marks:** 4

```python
from collections import Counter


class Solution:

  def search(self, pat, txt):
    k = len(pat)
    n = len(txt)
    if k > n:
      return 0

    pat_count = Counter(pat)
    window_count = Counter(txt[:k])

    ans = 0
    if pat_count == window_count:
      ans += 1

    for i in range(k, n):
      # Add the next character in the window
      window_count[txt[i]] += 1

      # Remove the first character of the previous window
      old_char = txt[i - k]
      window_count[old_char] -= 1
      if window_count[old_char] == 0:
        del window_count[old_char]

      # Compare window frequency with pattern frequency
      if pat_count == window_count:
        ans += 1

    return ans
```

*Generated on: 14/11/2026, 21:45:12*