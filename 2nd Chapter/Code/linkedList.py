class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        print(new_element.value, new_element.next)
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element


e1 = Element(1)
e2 = Element(2)
e3 = Element(3)

ll = LinkedList()
ll.append(e2)
# ll.append(e3)
