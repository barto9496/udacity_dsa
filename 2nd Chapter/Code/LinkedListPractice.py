"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom.
# There isn't a built-in data structure in Python that looks like a linked list. 
# Thankfully, it's easy to make classes that represent data structures in Python!
"""


class Element(object):
    """ All classes have a built-in init function, which is always executed when the class is being initiated.
    Use the __init__() function to assign values to object properties, or other operations that are necessary to do
    when the object is being created:

    Example:
        class Person:
            def __init__(self,name,age):
                self.name = name
                self.age = age

        p1 = Person("john", 25)
        print(p1.name)
        print(p1,age)
    """
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        counter = 1
        current = self.head
        if position > 0:
            while current and counter <= position:
                if counter == position:
                    return current
                current = current.next
                counter += 1
            return None
        else:
            return None


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
print(ll.get_position(4).value)
