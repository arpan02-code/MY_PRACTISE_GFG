## 01. Easy C++ Solution

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1)

### Problem Description

**Task:** Given a sorted doubly linked list containing distinct positive integers and an integer target, find all pairs of nodes whose values add up to target.

#### Examples

##### Example 1

- **Input:**
```text
target = 7
```
- **Output:**
```text
[[1, 6], [2, 5]]
```
- **Explanation:** There are two pairs (1, 6) and (2,5) with sum 7.

##### Example 2

- **Output:**
```text
[[1, 5]]
```
- **Explanation:** There is one pairs (1, 5) with sum 6.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-11-27 21:39:11
- **Status:** Correct
- **Marks:** 2

```python
# Structure of Doubly Linked List Node
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def givenSumPairs(self, head, target):
        if not head:
            return []

        left = head
        right = head
        while right.next:
            right = right.next

        pairs = []
        while left != right and right.next != left:
            curr_sum = left.data + right.data
            if curr_sum == target:
                pairs.append([left.data, right.data])
                left = left.next
                right = right.prev
            elif curr_sum < target:
                left = left.next
            else:
                right = right.prev

        return pairs
```

*Generated on: 27/11/2026, 21:39:32*