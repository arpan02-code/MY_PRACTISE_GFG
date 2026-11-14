## 01. Implement Stack using Array

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/implement-stack-using-array/1)

### Problem Description

**Task:** Implement a Stack using an Array, where the size of the array, n is given. The Stack must support the following operations:(i) push(x): Insert an element x at the top of the stack.(ii) pop(): Remove the element from the top of the stack.(iii) peek(): Return the top element if not empty, else -1.(iv) isEmpty(): Return true if the stack is empty else return false.(v) isFull(): Return true if the stack is full else return false.There will be a sequence of queries queries[][]. The queries are represented in numeric form: 1 x : Call push(x)2 : Call pop() 3 : Call peek()4 : Call isEmpty()5 : Call isFull()You just have to implement the functions push, pop, peek, isEmpty, and isFull. The driver code will handle the output.Note: All the queries are valid.Examples:Input: n = 3, queries[][] = [[1, 5], [1, 3], [3], [2], [4], [5]]

#### Examples

##### Example 1

- **Output:**
```text
[-1, -1, true, true]
```
- **Explanation:** Queries on stack are as follows:pop(): Since stack is empty, nothing is popped.peek(): Return the top element. Since the stack is empty, return -1.isEmpty(): Return true as the stack is empty.push(9): Insert 9 at the top of the stack. The stack will be [9].isFull(): Return true as the stack is full. Capacity = 1.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(1)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (2)

#### Solution 1 (Python)

- **Submitted:** 2026-11-14 21:46:52
- **Status:** Correct
- **Marks:** 0

```python
class myStack:
    def __init__(self, n):
        self.size = n
        self.arr = [0] * n
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.size - 1

    def push(self, x):
        if self.isFull():
            return
        self.top += 1
        self.arr[self.top] = x

    def pop(self):
        if self.isEmpty():
            return -1
        x = self.arr[self.top]
        self.top -= 1
        return x

    def peek(self):
        if self.isEmpty():
            return -1
        return self.arr[self.top]
```

#### Solution 2 (Python)

- **Submitted:** 2026-11-11 17:51:26
- **Status:** Correct
- **Marks:** 1

```python
class myStack:
    def __init__(self, n):
        self.size = n
        self.arr = [0] * n
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.size - 1

    def push(self, x):
        if self.isFull():
            return
        self.top += 1
        self.arr[self.top] = x

    def pop(self):
        if self.isEmpty():
            return -1
        x = self.arr[self.top]
        self.top -= 1
        return x

    def peek(self):
        if self.isEmpty():
            return -1
        return self.arr[self.top]
```

*Generated on: 14/11/2026, 21:47:11*