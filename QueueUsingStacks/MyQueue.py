class Node:
    def __init__(self, item, nxt=None):
        self.item = item
        self.next = nxt

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        self.head = Node(item, self.head)

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        item = self.head.item
        self.head = self.head.next
        return item

    @property
    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        else:
            return self.head.item

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

class MyQueue:
    def __init__(self):
        self._data_stack = Stack()

    def push(self, x: int) -> None:
        self._data_stack.push(x)

    def pop(self) -> int:
        reversed_stack = Stack()

        while self._data_stack:
            reversed_stack.push(self._data_stack.pop())

        res = reversed_stack.pop()

        while reversed_stack:
            self._data_stack.push(reversed_stack.pop())

        return res

    def peek(self) -> int:
        reversed_stack = Stack()

        while self._data_stack:
            reversed_stack.push(self._data_stack.pop())

        res = reversed_stack.peek

        while reversed_stack:
            self._data_stack.push(reversed_stack.pop())

        return res

    def empty(self) -> bool:
        return len(self._data_stack) == 0
