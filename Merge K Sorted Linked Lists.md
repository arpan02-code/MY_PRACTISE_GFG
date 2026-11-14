## 01. Merge K Sorted Linked Lists

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/merge-k-sorted-linked-lists/1)

### Problem Description

**Task:** Given an array arr[] of n sorted linked lists of different sizes. Your task is to merge all these lists into a single sorted linked list and return the head of the merged list.Examples:Input:

#### Examples

##### Example 1

- **Output:**
```text
1 - > 2 - > 3 - > 4 - > 7 - > 8 - > 9Explanation: The arr[] has 3 sorted linked list of size 3, 3, 1.1st list: 1 - > 3 - > 72nd list: 2 - > 4 - > 83rd list: 9The merged list will be: Input: Output: 1 - > 3 - > 4 - > 5 - > 6 - > 8Explanation: The arr[] has 3 sorted linked list of size 2, 1, 3.1st list: 1 - > 32nd list: 83rd list: 4 - > 5 - > 6The merged list will be:
```

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n log n)
- **Expected Auxiliary Space Complexity:** O(n)

### Accepted Solutions (3)

#### Solution 1 (Python)

- **Submitted:** 2026-11-14 21:48:45
- **Status:** Correct
- **Marks:** 0

```python
''' Linked List Node Structure
class Node:
    def _init_(self, x):
        self.data = x
        self.next = None
'''

import heapq


class Solution:

  def mergeKLists(self, arr: list["Node"]) -> "Node":
    dummy = Node(0)
    curr = dummy
    pq = []

    for i, head in enumerate(arr):
      if head:
        heapq.heappush(pq, (head.data, i, head))

    while pq:
      val, i, node = heapq.heappop(pq)
      curr.next = node
      curr = curr.next
      if node.next:
        heapq.heappush(pq, (node.next.data, i, node.next))

    curr.next = None
    return dummy.next
```

#### Solution 2 (Python)

- **Submitted:** 2026-11-09 13:50:17
- **Status:** Correct
- **Marks:** 0

```python
''' Linked List Node Structure
class Node:
    def _init_(self, x):
        self.data = x
        self.next = None
'''

import heapq


class Solution:

  def mergeKLists(self, arr: list["Node"]) -> "Node":
    dummy = Node(0)
    curr = dummy
    pq = []

    for i, head in enumerate(arr):
      if head:
        heapq.heappush(pq, (head.data, i, head))

    while pq:
      val, i, node = heapq.heappop(pq)
      curr.next = node
      curr = curr.next
      if node.next:
        heapq.heappush(pq, (node.next.data, i, node.next))

    curr.next = None
    return dummy.next
```

#### Solution 3 (Python)

- **Submitted:** 2026-11-09 13:49:30
- **Status:** Correct
- **Marks:** 4

```python
''' Linked List Node Structure
class Node:
    def _init_(self, x):
        self.data = x
        self.next = None
'''

import heapq


class Solution:

  def mergeKLists(self, arr: list["Node"]) -> "Node":
    dummy = Node(0)
    curr = dummy
    pq = []

    for i, head in enumerate(arr):
      if head:
        heapq.heappush(pq, (head.data, i, head))

    while pq:
      val, i, node = heapq.heappop(pq)
      curr.next = node
      curr = curr.next
      if node.next:
        heapq.heappush(pq, (node.next.data, i, node.next))

    curr.next = None
    return dummy.next
```

*Generated on: 14/11/2026, 21:49:11*