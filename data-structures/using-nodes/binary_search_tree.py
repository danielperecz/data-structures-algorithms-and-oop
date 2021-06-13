class Node:
    def __init__(self, item=None):
        self.left = None
        self.right = None
        self.item = item


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

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

    @staticmethod
    def pre_order(_root):
        a = []

        def pre_order_wrapper(root):
            if root:
                a.append(str(root.item))
                pre_order_wrapper(root.left)
                pre_order_wrapper(root.right)

        pre_order_wrapper(_root)
        print("Pre-order: {}".format(" -> ".join(a)))

    @staticmethod
    def in_order(_root):
        a = []

        def in_order_wrapper(root):
            if root:
                in_order_wrapper(root.left)
                a.append(str(root.item))
                in_order_wrapper(root.right)

        in_order_wrapper(_root)
        print("In-order: {}".format(" -> ".join(a)))

    @staticmethod
    def post_order(_root):
        a = []

        def post_order_wrapper(root):
            if root:
                post_order_wrapper(root.left)
                post_order_wrapper(root.right)
                a.append(str(root.item))

        post_order_wrapper(_root)
        print("Post-order: {}".format(" -> ".join(a)))


if __name__ == "__main__":
    test_list = [1, 2, 3, 9, 4, 5, 6, 7, -4]
    bst = BST()

    for x in test_list:
        bst.add(x)

    bst.pre_order(bst.root)
    bst.in_order(bst.root)
    bst.post_order(bst.root)
