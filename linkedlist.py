class ListNode:
    def __init__(
        self,
        val=None,
        next=None
    ) -> object:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = None


    def insert_left(
        self,
        val=None
    ) -> None:
        new_node = ListNode(val)
        if (self.head is None):
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
    

    def insert_right(
        self,
        val=None
    ) -> None:
        new_node = ListNode(val)
        if (self.head is None):
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1


    def pop(
        self,
        index: int
    ) -> None:
        count = 0
        prev, curr = self.head, self.head.next
        if (
            (index == 0) and
            (self.head.next)
        ):
            self.head = self.head.next
            
        while (curr):
            if (count == index):
                if (curr.next):
                    prev.next = curr.next
                    curr.next = None
                    self.length -= 1
                    return
            print(prev.val)
            prev = curr
            curr = curr.next
            count += 1

    
    def getValues(
            self
    ) -> None:
        print("v----- getValues() -----v")
        current = self.head
        count = 0
        while current:
            print(f'Element {count}: {current.val}')
            current = current.next
            count += 1
        print("^----- getValues() -----^")

    
def populate(
    list
) -> None:
    elements = [x * 3 for x in range(10)]
    for x in elements:
        list.insert_right(x)

linky = LinkedList()
print(linky.length)
populate(linky)
print(linky.length)
linky.getValues()
linky.pop(4)
print(linky.length)
linky.getValues()