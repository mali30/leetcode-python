
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class LinkList():
    def __init__(self,head):
        self.head = head 

    def createNode(self, value):
        new_node = Node(value)
        new_node.setNext() = self.head 
        self.head = new_node 

    
def reverseLinkList(head):
    if head is None:
        return head
    
    current = head 
    prev = None
    while current:
        nnext = current.next 
        current.next = prev 
        prev = current 
        current = nnext 
    self.head = prev 
    return prev 

myNode = Node(1)
myNode = Node(2)
myNode = Node(3)

print(reverseLinkList(1,2,3,4,5))
