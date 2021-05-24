from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def __repr__(self):
        elements = []
        for element in self.queue:
            elements.append(str(element))
        return " -> ".join(elements)

    def isEmpty(self):
        return len(self.queue) == 0

    def length(self):
        return len(self.queue)

    # Add an item to the end of the list.
    def add(self, item):
        self.queue.append(item)

    # Remove the first item in the list.
    def remove(self):
        if not self.isEmpty():
            return self.queue.popleft()

    def peek(self):
        if not self.isEmpty():
            return self.queue[0]
