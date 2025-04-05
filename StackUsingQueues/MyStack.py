class Node:
    def __init__(self, item, nxt=None):
        self.item = item
        self.next = nxt

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        if self.head is None:
            self.tail = Node(item)
            self.head = self.tail
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    def pop(self):
        if self.head:
            item = self.head.item
            self.head = self.head.next
            return item
        raise ValueError("Queue is empty.")

    @property
    def peek(self):
        return self.head.item

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

class MyStack:
    def __init__(self):
        self._data_queue = Queue()

    def push(self, x: int) -> None:
        self._data_queue.add(x)

    def pop(self) -> int:
        for _ in range(len(self._data_queue) - 1):
            self._data_queue.add(self._data_queue.pop())

        return self._data_queue.pop()

    def top(self) -> int:
        for _ in range(len(self._data_queue) - 1):
            self._data_queue.add(self._data_queue.pop())

        res = self._data_queue.pop()
        self._data_queue.add(res)

        return res

    def empty(self) -> bool:
        return self._data_queue.is_empty()
