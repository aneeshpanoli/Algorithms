
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
    node = root
    while queue:
        node = queue.pop(0)
        if node:
            queue.append(node.left)
            queue.append(node.right)
            print(node.value)



if __name__ == '__main__':

    bt1 = Node(1)
    bt1.left = Node(2)
    bt1.right = Node(3)
    bt1.left.left = Node(4)
    bt1.left.right = Node(5)

    level_order(bt1)




