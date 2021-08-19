class Node:
    def __init__(self, data):
        self.previous = None
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Making the LinkedList iterable.
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # Making the LinkedList printable.
    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(str(node.data))
        return " -> ".join(nodes) if self.head is not None else "Empty"

    def head_insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            node = self.head
            node.previous = new_node
            new_node.next = node
            self.head = new_node

        self.size += 1

    def head_delete(self):
        if self.head is not None:
            node = self.head
            self.head = node.next
            self.size -= 1
            return node
        return None

    def tail_insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def tail_delete(self):
        if self.head is not None:
            node = self.tail

            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.tail = node.previous
                self.tail.next = None

            self.size -= 1
            return node
        return None
