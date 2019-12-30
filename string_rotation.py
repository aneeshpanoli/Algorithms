# author: Aneesh Panoli\

'''
you impliemt a circular linked list
by pointing the next of the last element to the first element

1. find if given string is a rotation of the other string

s = "watermelon"
s_rotated = "melonwater"

'''

class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        
    def make_from_str(self, string:str):
        head = ListNode()
        curr = head
        for c in string:
            new_node = ListNode(c)
            curr.next = new_node
            curr = curr.next
        return head.next
    
    def make_circular_str(self, string:str):
        head = ListNode()
        curr = head
        for c in string:
            new_node = ListNode(c)
            curr.next = new_node
            curr = curr.next
        curr.next = head.next 
        return head.next
    
    def print_node(self, head):
        s = ""
        counter = 0
        if head and head.val:
            while head:
                s += head.val
                head = head.next
                counter += 1
                if counter == 10 * 3:
                    break
            return s
        else:
            return ""
        

        

def is_rotated_string(s:str, s_rotated: str) -> bool:
    head = ListNode().make_circular_str(s_rotated) # Time O(n) space = O(2n)
    counter = 0
    while head: # 0(1.5m)
        matched = True
        for c in s:  #o(n)
            if head.val != c:
                matched = False
                head = head.next
                break
            head = head.next
            counter += 1
        if matched:
            return True
        elif counter >= int(len(s)*1.5): 
            return False
        
def check_cycle(s:str) -> bool:
    head = ListNode().make_circular_str(s)
    unique = set()
    while head:
        if head in unique:
            return True
        else:
            unique.add(head)
        head = head.next
    return False
           
#total complexity will be o(1.5m * 0(1n)) -> O(mn)             
        
 
# print(is_rotated_string("Primerib", "RibPrime"))
print(check_cycle("abc"))
            
            
        
        

        
        
        
