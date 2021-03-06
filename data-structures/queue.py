from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def __repr__(self):
        elements = (str(element) for element in self.queue)
        return " -> ".join(elements)

    def is_empty(self):
        return len(self.queue) == 0

    def length(self):
        return len(self.queue)

    # Add an item to the end of the list.
    def enqueue(self, item):
        self.queue.append(item)

    # Remove the first item in the list.
    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
