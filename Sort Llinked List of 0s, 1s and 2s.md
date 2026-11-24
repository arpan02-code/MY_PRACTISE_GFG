## 01. Sort Llinked List of 0s, 1s and 2s

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1)

### Problem Description

**Task:** Given a linked list where nodes can contain values 0s, 1s, and 2s only. Your task is to rearrange the list so that all 0s appear at the beginning, followed by all 1s, and all 2s are placed at the end.Examples:Input: head = 1 → 2 → 2 → 1 → 2 → 0 → 2 → 2 Output: 0 → 1 → 1 → 2 → 2 → 2 → 2 → 2Explanation: All the 0s are segregated to the left end of the linked list, 2s to the right end of the list, and 1s in between. The final list will be: Input: head = 2 → 2 → 0 → 1 Output: 0 → 1 → 2 → 2Explanation: After arranging all the 0s, 1s and 2s in the given format, the output will be:

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-11-24 22:46:00
- **Status:** Correct
- **Marks:** 4

```python
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def segregate(self, head):
        if not head or not head.next:
            return head

        zero_head = Node(-1)
        one_head = Node(-1)
        two_head = Node(-1)

        zero = zero_head
        one = one_head
        two = two_head

        curr = head
        while curr:
            if curr.data == 0:
                zero.next = curr
                zero = zero.next
            elif curr.data == 1:
                one.next = curr
                one = one.next
            else:
                two.next = curr
                two = two.next
            curr = curr.next

        zero.next = one_head.next if one_head.next else two_head.next
        one.next = two_head.next
        two.next = None

        return zero_head.next
```

*Generated on: 24/11/2026, 22:46:22*