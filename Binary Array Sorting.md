## 01. Binary Array Sorting

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/binary-array-sorting-1587115620/1)

### Problem Description

**Task:** You are given a binary array arr[], where each element is either 0 or 1. Your task is to rearrange the array in increasing order in place (without using extra space). You do not need to return anything; simply modify the input array.

#### Examples

##### Example 1

- **Input:**
```text
arr[] = [1, 0, 1, 1, 0]
```
- **Output:**
```text
[0, 0, 1, 1, 1]
```
- **Explanation:** After arranging the elements in increasing order, elements will be as 0 0 1 1 1.

##### Example 2

- **Input:**
```text
arr[] = [1, 0, 1, 1, 1, 1, 1, 0, 0, 0]
```
- **Output:**
```text
[0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
```
- **Explanation:** After arranging the elements in increasing order, elements will be 0 0 0 0 1 1 1 1 1 1.

##### Example 3

- **Input:**
```text
arr[] = [1, 1, 1, 1]
```
- **Output:**
```text
[1, 1, 1, 1]
```
- **Explanation:** Since the array already contains only 1s, no change is needed.

#### Constraints

- **1.** `1 ≤ arr.size() ≤ 10⁶arr[i] ∈ {0,1} for all valid indices i.`

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (5)

#### Solution 1 (Python)

- **Submitted:** 2026-10-04 12:58:41
- **Status:** Correct
- **Marks:** 0

```python
class Solution:
    def binSort(self, arr):
        # code here
        l= 0
        r= len(arr)-1
        
        while l<r:
            
            while l<r and arr[l]==0:
                l+=1
                
            while  l<r and arr[r]==1:
                r-=1
            
            else :
                
                arr[l], arr[r]= arr[r] , arr[l]
                
                l+=1
                r-=1
```

#### Solution 2 (Python)

- **Submitted:** 2026-10-04 12:48:36
- **Status:** Correct
- **Marks:** 0

```python
class Solution:
    def binSort(self, arr):
        # code here
        l= 0
        r= len(arr)-1
        
        while l<r:
            
            while l<r and arr[l]==0:
                l+=1
                
            while  l<r and arr[r]==1:
                r-=1
            
            else :
                
                arr[l], arr[r]= arr[r] , arr[l]
                
                l+=1
                r-=1
```

#### Solution 3 (Python)

- **Submitted:** 2026-10-04 12:45:14
- **Status:** Correct
- **Marks:** 0

```python
class Solution:
    def binSort(self, arr):
        # code here
        l= 0
        r= len(arr)-1
        
        while l<r:
            
            while l<r and arr[l]==0:
                l+=1
                
            while  l<r and arr[r]==1:
                r-=1
            
            else :
                
                arr[l], arr[r]= arr[r] , arr[l]
                
                l+=1
                r-=1
```

#### Solution 4 (Python)

- **Submitted:** 2026-10-04 12:22:22
- **Status:** Correct
- **Marks:** 0

```python
class Solution:
    def binSort(self, arr):
        # code here
        l= 0
        r= len(arr)-1
        
        while l<r:
            
            while l<r and arr[l]==0:
                l+=1
                
            while  l<r and arr[r]==1:
                r-=1
            
            else :
                
                arr[l], arr[r]= arr[r] , arr[l]
                
                l+=1
                r-=1
```

#### Solution 5 (Python)

- **Submitted:** 2026-10-04 09:40:05
- **Status:** Correct
- **Marks:** 0

```python
class Solution:
    def binSort(self, arr):
        # code here
        l= 0
        r= len(arr)-1
        
        while l<r:
            
            while l<r and arr[l]==0:
                l+=1
                
            while  l<r and arr[r]==1:
                r-=1
            
            else :
                
                arr[l], arr[r]= arr[r] , arr[l]
                
                l+=1
                r-=1
```

*Generated on: 04/10/2026, 12:59:08*