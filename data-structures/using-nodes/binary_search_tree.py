class Node:
    def __init__(self, item=None):
        self.left = None
        self.right = None
        self.item = item

    def __iter__(self):
        # In-order iteration.
        if self.left:
            yield from self.left    # Works like: for node in self.left: yield node
        yield self
        if self.right:
            yield from self.right

    def __repr__(self):
        return str(self.item)


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __iter__(self):
        if self.root:
            return iter(self.root)
        return iter(())

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(str(node.item))
        return " -> ".join(nodes)

    def add(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            parent = None
            subtree = self.root
            while subtree is not None:
                parent = subtree
                if item < subtree.item:
                    subtree = subtree.left
                else:
                    subtree = subtree.right
            if item < parent.item:
                parent.left = Node(item)
            else:
                parent.right = Node(item)
        self.size += 1

    def print_pre_order(self):
        a = []

        def pre_order(root):
            if root:
                a.append(str(root.item))
                pre_order(root.left)
                pre_order(root.right)

        pre_order(self.root)
        print("Pre-order: {}".format(" -> ".join(a)))

    def print_in_order(self):
        a = []

        def in_order(root):
            if root:
                in_order(root.left)
                a.append(str(root.item))
                in_order(root.right)

        in_order(self.root)
        print("In-order: {}".format(" -> ".join(a)))

    def print_post_order(self):
        a = []

        def post_order(root):
            if root:
                post_order(root.left)
                post_order(root.right)
                a.append(str(root.item))

        post_order(self.root)
        print("Post-order: {}".format(" -> ".join(a)))


if __name__ == "__main__":
    test_list = [1, 2, 3, 9, 4, 5, 6, 7, -4]
    bst = BST()

    for x in test_list:
        bst.add(x)

    bst.print_pre_order()
    bst.print_in_order()
    bst.print_post_order()

    print(bst)
