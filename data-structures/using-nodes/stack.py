class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __iter__(self):
        node = self.top
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(str(node.data))
        return " -> ".join(nodes)

    def isEmpty(self):
        return self.top is None

    def length(self):
        return self.size

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if not self.isEmpty():
            item = self.top.data
            self.top = self.top.next
            self.size -= 1
            return item

    def peek(self):
        if not self.isEmpty():
            return self.top.data
