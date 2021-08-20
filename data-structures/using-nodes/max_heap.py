class MaxHeap:
    def __init__(self):
        self.__heap = []

    def root_node(self):
        return self.__heap[0] if self.__heap else None

    def last_node(self):
        return self.__heap[-1] if self.__heap else None

    def insert(self, data):
        # Function inserts data at the end of the heap and executes the trickle-up algorithm (up-heap operation).
        self.__heap.append(data)
        new_node_index = len(self.__heap) - 1
        while new_node_index > 0 and self.__heap[new_node_index] > self.__heap[self.parent_index(new_node_index)]:
            parent_index = self.parent_index(new_node_index)
            self.__heap[parent_index], self.__heap[new_node_index] = self.__heap[new_node_index], self.__heap[parent_index]
            new_node_index = parent_index

    def delete(self):
        # Function replaces root node with last node and executes the trickle-down algorithm (down-heap operation).
        if len(self.__heap) <= 1:
            self.__heap = []
        else:
            # Replace root node with last node.
            self.__heap[0] = self.__heap.pop()

            trickle_node_index = 0
            while self.has_greater_child(trickle_node_index):
                larger_child_index = self.larger_child_index(trickle_node_index)

                # Swap trickle node with larger child.
                self.__heap[trickle_node_index], self.__heap[larger_child_index] = \
                    self.__heap[larger_child_index], self.__heap[trickle_node_index]

                trickle_node_index = larger_child_index

    def has_greater_child(self, index):
        left_child = self.__heap[self.left_child_index(index)] if self.valid_index(self.left_child_index(index)) else None
        right_child = self.__heap[self.right_child_index(index)] if self.valid_index(self.right_child_index(index)) else None
        parent = self.__heap[index]
        return (left_child is not None and left_child > parent) or (right_child is not None and right_child > parent)

    def larger_child_index(self, index):
        if not self.__heap[self.right_child_index(index)]:
            return self.left_child_index(index)
        if self.__heap[self.right_child_index(index)] > self.__heap[self.left_child_index(index)]:
            return self.right_child_index(index)
        return self.left_child_index(index)

    def valid_index(self, index):
        return (0 <= index) and (index < len(self.__heap))

    @staticmethod
    def parent_index(index):
        return (index - 1) // 2

    @staticmethod
    def left_child_index(index):
        return (index * 2) + 1

    @staticmethod
    def right_child_index(index):
        return (index * 2) + 2
