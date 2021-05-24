class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def __iter__(self):
        node = self.first
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(str(node.data))
        return " -> ".join(nodes)

    def isEmpty(self):
        return self.first is None

    def length(self):
        return self.size

    # Add an item to the end of the list.
    def add(self, item):
        new_node = Node(item)
        if self.last is not None:
            self.last.next = new_node
        
        self.last = new_node
        if self.first is None:
            self.first = self.last

        self.size += 1

    # Remove the first item in the list.
    def remove(self):
        if not self.isEmpty():
            item = self.first.data
            self.first = self.first.next
            if self.first is None:
                self.last = None
            self.size -= 1
            return item

    def peek(self):
        if not self.isEmpty():
            return self.first.data
