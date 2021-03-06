from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def __repr__(self):
        elements = (str(element) for element in self.stack)
        return " -> ".join(elements)

    def is_empty(self):
        return len(self.stack) == 0

    def length(self):
        return len(self.stack)

    def push(self, item):
        self.stack.appendleft(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.popleft()
