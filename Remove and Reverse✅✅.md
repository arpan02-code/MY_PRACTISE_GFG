## 01. Remove and Reverse✅✅

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/remove-and-reverse--170634/1)

### Problem Description

**Task:** Given a string s which consists of only lowercase English alphabets.You need to perform the below operations while there is a repeating characterRemove the first repeating character and reverse the stringAgain perform the above operation on the modified string if there is a repeating character.Find the final string after all possible operations.Examples:Input: s = "abab"

#### Examples

##### Example 1

- **Output:**
```text
"d"
```
- **Explanation:** In 1st operation the first repeating character is 'd'. After Removing the first character, s = "ddd". After Reversing the string, s = "ddd". In 2nd operation, Similarly, s = "dd". In 3rd operation, Similarly, s = "d". Now the string s does not contain any repeating character.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-10-10 20:33:54
- **Status:** Correct
- **Marks:** 4

```python
class Solution:
    def removeReverse(self, s: str) -> str:
        from collections import Counter

        freq = Counter(s)
        deq = list(s)

        i, j = 0, len(s) - 1
        left_to_right = True

        while i <= j:
            if left_to_right:
                if freq[deq[i]] > 1:
                    freq[deq[i]] -= 1
                    deq[i] = ""
                    left_to_right = False
                i += 1
            else:
                if freq[deq[j]] > 1:
                    freq[deq[j]] -= 1
                    deq[j] = ""
                    left_to_right = True
                j -= 1

        res = [c for c in deq if c != ""]
        if not left_to_right:
            res.reverse()

        return "".join(res)
```

*Generated on: 10/10/2026, 20:34:09*