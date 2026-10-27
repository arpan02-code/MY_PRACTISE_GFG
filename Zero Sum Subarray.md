## 01. Zero Sum Subarray

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1)

### Problem Description

**Task:** Given an array of integers, arr[]. Find if there is a subarray (of size at least one) with 0 sum. Return true/false depending upon whether there is a subarray present with 0-sum or not. Examples:Input: arr[] = [4, 2, -3, 1, 6]

#### Examples

##### Example 1

- **Output:**
```text
false
```
- **Explanation:** 0 is one of the elements in the array so there exist a subarray with sum 0.Input: arr = [1, 2, -1]

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(n)

### Accepted Solutions (2)

#### Solution 1 (Python)

- **Submitted:** 2026-10-27 20:40:06
- **Status:** Correct
- **Marks:** 0

```python
class Solution:
    def subArrayExists(self, arr):
        # code here
        s= {0}
        curr =0
        
        for x in arr :
            curr += x
            
            if curr in s:
                return True 
            s.add(curr)
        return False
```

#### Solution 2 (Python)

- **Submitted:** 2026-10-25 20:36:49
- **Status:** Correct
- **Marks:** 4

```python
class Solution:
    def subArrayExists(self, arr):
        # code here
        s= {0}
        curr =0
        
        for x in arr :
            curr += x
            
            if curr in s:
                return True 
            s.add(curr)
        return False
```

*Generated on: 27/10/2026, 20:40:27*