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
        self.length = 0


    def insert(
        self,
        val=None,
        index=-1
    ) -> None:
        if (index < 0):
            target = self.length + 1 + index
        else:
            target = index
        new_node = ListNode(val)
        count = 0
        if (self.head is None):
            self.head = new_node
            self.tail = new_node
            self.length += 1
        elif (target in (-1, self.length)):
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        elif (target == 0):
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        else:
            prev, curr = self.head, self.head.next
            while (curr):
                count += 1
                if (count == target):
                    new_node.next = curr
                    prev.next = new_node
                    return
                prev = curr
                curr = curr.next
            print("INDEX NOT FOUND")


    def pop(
        self,
        index=-1
    ) -> None:
        if (index < 0):
            target = self.length + index
        else:
            target = index
        if (
            (target == 0) and
            (self.head.next)
        ):
            self.head = self.head.next
            
        count = 0
        prev, curr = self.head, self.head.next
        while (curr):
            count += 1
            if (count == target):
                prev.next = curr.next
                curr.next = None
                self.length -= 1
                return
            prev = curr
            curr = curr.next

    
    def getValues(
        self
    ) -> None:
        print("v----- getValues() -----v")
        current = self.head
        count = 0
        while current:
            print(f'Index {count}: {current.val}')
            current = current.next
            count += 1
        print("^----- getValues() -----^")

    
    def getElement(
        self,
        index: int
    ) -> None:
        if (index < 0):
            target = self.length + index
        else:
            target = index
        current = self.head
        count = 0
        while (current):
            if (count == target):
                print(f'\n---FOUND---\nIndex: {target}\nValue: {current.val}\n---FOUND---\n')
                return
            current = current.next
            count += 1
        print(f'ELEMENT NOT FOUND')
    
def populate(
    list
) -> None:
    elements = [x * 3 for x in range(10)]
    for x in elements:
        list.insert(x)

linky = LinkedList()
populate(linky)
print(linky.length)
linky.getValues()
linky.getElement(-1)
linky.pop()
linky.getValues()
linky.getElement(-2)