from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def in_order(self, root):
        if not root:
            return None
        
        self.in_order(root.left)
        print(root.val)
        self.in_order(root.right)
    
    def print_right(self, root):
        values = []
        return self.traverse(root, values, 0)
        
    def traverse(self, root, values, depth):
        if not root:
            return
        if depth == len(values):
            values.append(root.val)
        print(values)
        self.traverse(root.right, values, depth + 1)
        self.traverse(root.left, values, depth + 1)
        return values
    
    def bfs_queue(self, root):
        queue = deque([])
        queue.append((root, 0))
        
        values = []
        while queue:
            curr, depth = queue.popleft()
            if curr:
                if depth == len(values):
                    values.append(curr.val)
                queue.append((curr.right, depth +1))
                queue.append((curr.left, depth +1))
        return values
    
    def dfs_stack(self, root):
        stack = []
        values = []
        stack.append((root, 0))
        while stack:
            curr, depth = stack.pop()
            if curr:
                if depth == len(values):
                    values.append(curr.val)
                stack.append((curr.left, depth + 1))
                stack.append((curr.right, depth + 1))
        return values
                    
            
        
        
        
        
    
        
        
bt = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(5), TreeNode(4, TreeNode(6))))

bt.in_order(bt)

print(bt.dfs_stack(bt))
