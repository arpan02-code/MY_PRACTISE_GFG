## 01. Indexes of Subarray Sum

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1)

### Problem Description

**Task:** Given an array arr[] containing only non-negative integers, find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value target . You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. You need to find the first subarray whose sum is equal to the target. If no such array is possible then, return [-1].Examples:Input: arr[] = [1, 2, 3, 7, 5], target = 12

#### Examples

##### Example 1

- **Output:**
```text
[1, 5]
```
- **Explanation:** The sum of elements from 1st to 5th position is 15.

##### Example 2

- **Input:**
```text
arr[] = [5, 3, 4], target = 2
```
- **Output:**
```text
[-1]
```
- **Explanation:** There is no subarray with sum 2.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (2)

#### Solution 1 (Python)

- **Submitted:** 2026-11-14 21:52:18
- **Status:** Correct
- **Marks:** 0

```python
class Solution:
    def subarraySum(self, arr: list[int], target: int) -> list[int]:
        # code here
        i = 0  #start
        c_s= 0     # currrent sum 
        
        for j in range(len(arr)):                                    #j= end
            c_s += arr[j]
            
            while c_s > target and  i< j :
                c_s -= arr[i]
                i += 1
                
            if c_s == target:
                return[i+1,j+1]
                
        return [-1]
```

#### Solution 2 (Python)

- **Submitted:** 2026-11-06 12:00:57
- **Status:** Correct
- **Marks:** 4

```python
class Solution:
    def subarraySum(self, arr: list[int], target: int) -> list[int]:
        # code here
        i = 0  #start
        c_s= 0     # currrent sum 
        
        for j in range(len(arr)):                                    #j= end
            c_s += arr[j]
            
            while c_s > target and  i< j :
                c_s -= arr[i]
                i += 1
                
            if c_s == target:
                return[i+1,j+1]
                
        return [-1]
```

*Generated on: 14/11/2026, 21:52:39*