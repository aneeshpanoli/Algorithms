#author Aneesh Panoli
'''
while not root.next, root.next newnode9value
'''


from typing import Iterable, List, Any

class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        
    def print_list(self, head):
        while head:
            print(head.val)
            head = head.next
        return

    
class BinaryTreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left
        
    def make_tree_from_iter(self, src: Iterable):
        src_processed = self.process_iterable(src)
        print(src_processed)
        root = BinaryTreeNode(val=src_processed[0])
        for i in src_processed[1:]:
            curr = root
            while curr:
                if i <= curr.val:
                    if not curr.left: 
                        curr.left = BinaryTreeNode(val=i)
                        break
                    curr = curr.left
                elif i > curr.val:
                    if not curr.right: 
                        curr.right = BinaryTreeNode(val=i)
                        break
                    curr = curr.right          
        return root              
            
    def in_order(self, root, data: List[Any]):
        if not root:
            return None
        self.in_order(root.left, data)
        data.append(root.val)
        self.in_order(root.right, data)  
        return data
        
    def process_iterable(self, src: Iterable):
        src.sort()
        return src[:len(src)//2][::-1] + src[len(src)//2:]
    
    def binary_tree_to_linked_list(self, data):
        
        head = curr = ListNode()
        for i in data:
            curr.next = ListNode(val=i)
            curr = curr.next
        return head.next
        
    
    
    
bt = BinaryTreeNode()
root = bt.make_tree_from_iter([6, 5, 7, 8])
data = root.in_order(root, [])
linked_list = root.binary_tree_to_linked_list(data)
print(ListNode().print_list(linked_list))