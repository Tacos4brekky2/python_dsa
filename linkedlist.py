class ListNode:
    def __init__(
        self,
        val=None
    ) -> object:
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def insert_left(
        self,
        val=None
    ) -> None:
        new_node = ListNode(val)
        if (self.head is None):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    

    def insert_right(
        self,
        val=None
    ) -> None:
        new_node = ListNode(val)
        if (self.head is None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    
    def linearTraversal(
            self
    ) -> None:
        current = self.head
        while current:
            print(f'\nValue: {current.val}')
            current = current.next



linky = LinkedList()
linky.insert_left(42)
linky.insert_right(69)
linky.insert_left(55)
linky.linearTraversal()
print(linky.head.next)