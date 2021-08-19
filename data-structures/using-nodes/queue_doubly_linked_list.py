from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.__queue = DoublyLinkedList()

    def __repr__(self):
        elements = (str(element) for element in self.__queue)
        return " -> ".join(elements)

    def enqueue(self, data):
        self.__queue.tail_insert(data)

    def dequeue(self):
        removed_node = self.__queue.head_delete()
        return removed_node

    def size(self):
        return self.__queue.size

    def peek(self):
        return self.__queue.head

    def is_empty(self):
        return self.__queue.head is None
