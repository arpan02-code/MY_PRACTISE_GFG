## 01. Linked List End Insertion

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/linked-list-insertion-1587115620/1)

### Problem Description

**Task:** You are given the head of a Singly Linked List and a value x, insert that value x at the end of the LinkedList and return the head of the modified Linked List.Examples :Input: x = 6, Output: 1 - > 2 - > 3 - > 4 - > 5 - > 6

#### Examples

##### Example 1

- **Explanation:** We can see that 6 is inserted at the end of the linkedlist.

##### Example 2

- **Input:**
```text
x = 1, Output: 4 - > 5 - > 1Explanation: We can see that 1 is inserted at the end of the linked list.
```

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (3)

#### Solution 1 (Python)

- **Submitted:** 2026-11-14 21:47:33
- **Status:** Correct
- **Marks:** 0

```python
'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def insertAtEnd(self, head, x):
        # Step 1: Naya node create karo
        new_node = Node(x)

        # Step 2: Agar Linked List khali hai
        if head is None:
            return new_node

        # Step 3: Aakhri node tak travel karo
        curr = head
        while curr.next is not None:
            curr = curr.next

        # Step 4: Aakhri node ke next me naya node laga do
        curr.next = new_node

        # Step 5: Head return kar do
        return head
```

#### Solution 2 (Python)

- **Submitted:** 2026-11-10 09:52:09
- **Status:** Correct
- **Marks:** 0

```python
'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def insertAtEnd(self, head, x):
        # Step 1: Naya node create karo
        new_node = Node(x)

        # Step 2: Agar Linked List khali hai
        if head is None:
            return new_node

        # Step 3: Aakhri node tak travel karo
        curr = head
        while curr.next is not None:
            curr = curr.next

        # Step 4: Aakhri node ke next me naya node laga do
        curr.next = new_node

        # Step 5: Head return kar do
        return head
```

#### Solution 3 (Python)

- **Submitted:** 2026-11-10 09:51:57
- **Status:** Correct
- **Marks:** 1

```python
'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def insertAtEnd(self, head, x):
        # Step 1: Naya node create karo
        new_node = Node(x)

        # Step 2: Agar Linked List khali hai
        if head is None:
            return new_node

        # Step 3: Aakhri node tak travel karo
        curr = head
        while curr.next is not None:
            curr = curr.next

        # Step 4: Aakhri node ke next me naya node laga do
        curr.next = new_node

        # Step 5: Head return kar do
        return head
```

*Generated on: 14/11/2026, 21:47:54*