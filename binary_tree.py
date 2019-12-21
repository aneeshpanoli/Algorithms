
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def in_order(root):
    if not root:
        return None
    in_order(root.left)
    print(root.value)
    in_order(root.right)

def pre_order(root):
    if not root:
        return None
    print(root.value)
    in_order(root.left)
    in_order(root.right)

def post_order(root):
    if not root:
        return None

    in_order(root.left)
    in_order(root.right)
    print(root.value)

def level_order(root):
    queue = []
    queue.append(root)
    while queue:
        node = queue.pop(0)
        if node:
            queue.append(node.left)
            queue.append(node.right)
            print(node.value)


def make_tree(arr):
    queue = []
    node = root = Node(arr.pop(0))
    queue.append(node)
    while arr:
        node = queue.pop(0)
        child = Node(arr.pop(0))
        node.left = child
        queue.append(child)
        if arr:
            child = Node(arr.pop(0))
            node.right = child
            queue.append(child)
    return root

def make_bst(arr):
    node = root = Node(arr.pop(len(arr)//2))
    while arr:
        child = Node(arr.pop(0))
        if child.value > node.value:
            while node.right:
                node = node.right
            node.right = child
            node = root
        else:
            while node.left:
                node = node.left
            node.left = child
            node = root
    return root


def height(root):
    if not root:
        return -1
    else:
        return 1 + max(height(root.left), height(root.right))


if __name__ == '__main__':

    bt1 = Node(1)
    bt1.left = Node(2)
    bt1.right = Node(3)
    bt1.left.left = Node(4)
    bt1.left.right = Node(5)

    bt2 = make_bst(sorted([5, 1, 2, 3, 4, 6, 7]))

    # print(bt2.value)
    # in_order(bt2)
    print(height(bt2))




