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

    
    def getValues(
            self
    ) -> None:
        print("----- getValues() -----")
        current = self.head
        while current:
            print(f'Value: {current.val}')
            current = current.next
        print("----- getValues() -----")

def populate(
    list
) -> None:
    elements = [x * 3 for x in range(10)]
    for x in elements:
        list.insert_right(x)

linky = LinkedList()
populate(linky)
linky.getValues()