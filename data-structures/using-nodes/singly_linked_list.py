class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Making the LinkedList iterable.
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # Making the LinkedList printable.
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        return " -> ".join(nodes)

    def appendToHead(self, data):
        node = Node(data)
        node.next = self.head                                   # New node will point to current head
        self.head = node                                        # Now update head with new node
    
    def appendToTail(self, data):
        end = Node(data)
        if self.head is None:
            self.head = end
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = end

    def appendAfterValue(self, target_data, data):
        if self.head is not None and self.head.next is None:
            self.appendToTail(data)
        
        elif self.head is not None:
            target_node = Node(target_data)
            new_node = Node(data)
            node = self.head
            while node.next is not None:
                if node.data == target_node.data:
                    new_node.next = node.next
                    node.next = new_node
                    break
                node = node.next

    def deleteValue(self, data):
        if self.head is not None:
            target_node = Node(data)
            if self.head.data == target_node.data:
                self.head = self.head.next
            else:
                previous_node = self.head
                for node in self:                               # This works since we yield node in __iter__.
                    if node.data == target_node.data:
                        previous_node.next = node.next
                        break
                    previous_node = node
