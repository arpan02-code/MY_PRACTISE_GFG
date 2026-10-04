## 01. Search in a Matrix

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/search-in-a-matrix--021840/1)

### Problem Description

**Task:** Given a 2D integer array mat[][] of n rows and m columns and a number x, find whether element x is present in the matrix or not.

#### Examples

##### Example 1

- **Input:**
```text
mat[][] = [[6, 23, 21], [4, 45, 32], [69, 11, 87]], x = 32
```
- **Output:**
```text
true
```
- **Explanation:** 32 is present in the matrix.

##### Example 2

- **Input:**
```text
mat[][] = [[14, 34, 23, 95, 43, 28]], x = 55Output: false
```
- **Explanation:** 55 is not present in the matrix.

##### Example 3

- **Input:**
```text
mat[][] = [[87, 9, 99], [101, 3, 111]], x = 101Output: true
```
- **Explanation:** 101 is present in the matrix.

#### Constraints

- **1.** `1 ≤ n, m ≤ 5001 ≤ mat[][] ≤ 10⁵¹ ≤ x ≤ 10⁵`

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n * m)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (5)

#### Solution 1 (Python)

- **Submitted:** 2026-10-04 13:04:02
- **Status:** Correct
- **Marks:** 0

```python
#User function Template for python3

class Solution:

    #Function to search a given integer in a matrix.
    def searchMatrix(self,matrix, x): 
        for row  in matrix : 
            for element in row :
                if element == x: 
                    return 1
```

#### Solution 2 (Python)

- **Submitted:** 2026-10-04 13:03:20
- **Status:** Correct
- **Marks:** 0

```python
#User function Template for python3

class Solution:

    #Function to search a given integer in a matrix.
    def searchMatrix(self,matrix, x): 
        for row  in matrix : 
            for element in row :
                if element == x: 
                    return 1
```

#### Solution 3 (Python)

- **Submitted:** 2026-01-25 11:18:28
- **Status:** Correct
- **Marks:** 0

```python
#User function Template for python3

class Solution:
    
    #Function to search a given integer in a matrix.
    def searchMatrix(self,matrix, x): 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == x:
                    return 1 
                
        return 0
```

#### Solution 4 (Python)

- **Submitted:** 2026-01-23 10:42:38
- **Status:** Correct
- **Marks:** 0

```python
#User function Template for python3

class Solution:
    
    #Function to search a given integer in a matrix.
    def searchMatrix(self,matrix, x): 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == x:
                    return 1 
                
        return 0
```

#### Solution 5 (Python)

- **Submitted:** 2026-01-23 10:42:25
- **Status:** Correct
- **Marks:** 0

```python
#User function Template for python3

class Solution:
    
    #Function to search a given integer in a matrix.
    def searchMatrix(self,matrix, x): 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == x:
                    return 1 
                
        return 0
```

*Generated on: 04/10/2026, 13:04:27*