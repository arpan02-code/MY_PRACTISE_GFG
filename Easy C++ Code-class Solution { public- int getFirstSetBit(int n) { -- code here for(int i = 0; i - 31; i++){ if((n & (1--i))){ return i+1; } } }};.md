## 01. Easy C++ Code:class Solution { public: int getFirstSetBit(int n) { // code here for(int i = 0; i < 31; i++){ if((n & (1<<i))){ return i+1; } } }};

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/find-first-set-bit-1587115620/1)

### Problem Description

**Task:** Given an integer n. You have to return the position of the first set bit from the right side in the binary representation of the number. If there is no set bit in the integer N, then return 0 from the function. Examples:Input: n = 18

#### Examples

##### Example 1

- **Output:**
```text
1
```
- **Explanation:** Binary representation of 1 is 1, the first set bit from the right side is at position 1.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(log n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (2)

#### Solution 1 (Python)

- **Submitted:** 2026-11-14 21:45:31
- **Status:** Correct
- **Marks:** 0

```python
class Solution:
    def getFirstSetBit(self, n: int) -> int:
        if n == 0:
            return 0
        return (n & -n).bit_length()
```

#### Solution 2 (Python)

- **Submitted:** 2026-11-12 18:58:10
- **Status:** Correct
- **Marks:** 2

```python
class Solution:
    def getFirstSetBit(self, n: int) -> int:
        if n == 0:
            return 0
        return (n & -n).bit_length()
```

*Generated on: 14/11/2026, 21:46:09*