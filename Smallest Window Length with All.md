## 01. Smallest Window Length with All

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/smallest-distant-window3132/1)

### Problem Description

**Task:** Given a string s, your task is to find the length of the smallest window that contains all the characters of the given string at least once.Example:Input: s = "aabcbcdbca"

#### Examples

##### Example 1

- **Output:**
```text
4
```
- **Explanation:** Sub-String "dbca" has the smallest length that contains all the characters of string s.

##### Example 2

- **Input:**
```text
s = "aaab"
```
- **Output:**
```text
7
```
- **Explanation:** There are multiple substring with smallest length that contains all characters of string s, "eksforg" and "ksforge".

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (3)

#### Solution 1 (Python)

- **Submitted:** 2026-10-27 20:39:19
- **Status:** Correct
- **Marks:** 0

```python
class Solution:
    def findSubString(self, s):
        
        from collections import defaultdict
        # code here
        set_s = set(s)
        total_count = len(set_s)
        
        n = len(s)
        if total_count == 0 :
            return 0 
            
        
        char_count = defaultdict(int) # ye humare sare current winow me kitne charcter hai batayega 
        start = 0
        min_len = float('inf')
        
        count =0 
        
        # let's start sliding window 
        
        for j in range(n):
            if char_count[s[j]] ==0 :
                count+= 1
            char_count[s[j]] += 1
            
            while count == total_count:
                min_len = min(min_len, j - start + 1)
        
                char_count[s[start]] -= 1
                if char_count[s[start]] == 0:
                    count -= 1
                start += 1    
        
        return min_len
```

#### Solution 2 (Python)

- **Submitted:** 2026-10-26 13:55:54
- **Status:** Correct
- **Marks:** 0

```python
class Solution:
    def findSubString(self, s):
        
        from collections import defaultdict
        # code here
        set_s = set(s)
        total_count = len(set_s)
        
        n = len(s)
        if total_count == 0 :
            return 0 
            
        
        char_count = defaultdict(int) # ye humare sare current winow me kitne charcter hai batayega 
        start = 0
        min_len = float('inf')
        
        count =0 
        
        # let's start sliding window 
        
        for j in range(n):
            if char_count[s[j]] ==0 :
                count+= 1
            char_count[s[j]] += 1
            
            while count == total_count:
                min_len = min(min_len, j - start + 1)
        
                char_count[s[start]] -= 1
                if char_count[s[start]] == 0:
                    count -= 1
                start += 1    
        
        return min_len
```

#### Solution 3 (Python)

- **Submitted:** 2026-10-26 13:55:44
- **Status:** Correct
- **Marks:** 4

```python
class Solution:
    def findSubString(self, s):
        
        from collections import defaultdict
        # code here
        set_s = set(s)
        total_count = len(set_s)
        
        n = len(s)
        if total_count == 0 :
            return 0 
            
        
        char_count = defaultdict(int) # ye humare sare current winow me kitne charcter hai batayega 
        start = 0
        min_len = float('inf')
        
        count =0 
        
        # let's start sliding window 
        
        for j in range(n):
            if char_count[s[j]] ==0 :
                count+= 1
            char_count[s[j]] += 1
            
            while count == total_count:
                min_len = min(min_len, j - start + 1)
        
                char_count[s[start]] -= 1
                if char_count[s[start]] == 0:
                    count -= 1
                start += 1    
        
        return min_len
```

*Generated on: 27/10/2026, 20:39:36*