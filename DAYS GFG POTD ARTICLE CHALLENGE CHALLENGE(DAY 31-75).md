## 01. 75 DAYS GFG POTD ARTICLE CHALLENGE CHALLENGE(DAY 31/75)

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/find-duplicates-in-an-array/1)

### Problem Description

**Task:** Given an array arr[] of size n, containing elements from the range 1 to n, and each element appears at most twice, return an array of all the integers that appears twice.Note: You can return the elements in any order but the driver code will print them in sorted order.Examples:Input: arr[] = [2, 3, 1, 2, 3]

#### Examples

##### Example 1

- **Output:**
```text
[2, 3]
```
- **Explanation:** 2 and 3 occur more than once in the given array.Input: arr[] = [3, 1, 2] Output: []Explanation: There is no repeating element in the array, so the output is empty.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (2)

#### Solution 1 (Python)

- **Submitted:** 2026-11-02 20:07:02
- **Status:** Correct
- **Marks:** 0

```python
class Solution:
    def findDuplicates(self, arr):
        # code here
        f ={}
        count=0 
        for x in arr:
            f[x]= f.get(x,0)+1
        ans=[]
        
        for x ,count in f.items():
            if count >1:
                ans.append(x)
                
        return sorted(ans)
```

#### Solution 2 (Python)

- **Submitted:** 2026-11-02 20:06:51
- **Status:** Correct
- **Marks:** 2

```python
class Solution:
    def findDuplicates(self, arr):
        # code here
        f ={}
        count=0 
        for x in arr:
            f[x]= f.get(x,0)+1
        ans=[]
        
        for x ,count in f.items():
            if count >1:
                ans.append(x)
                
        return sorted(ans)
```

*Generated on: 02/11/2026, 20:07:26*