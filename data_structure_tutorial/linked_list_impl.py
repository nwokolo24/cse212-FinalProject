# Implementatin of linked list data structure in python

# Node Class implementation
class Node:
    """
    Each node contains a value and a pointer to a previous and next node
    """
    def __init__(self, value):
        """
        This initialise a node with a value provided

        Args:
            value (_type_): It could be any data type
        """
        self.value = value
        self.prev = None
        self.next = None

# Actual linked list class implementation
class LinkedList:
    """Below a linked list will be implemented and some of the operations we have seen in this document will be written in code.
    """
    def __init__(self):
        """Initialisatin of empty linked list
        """
        self.head = None
        self.tail = None

    def insert_at_head(self, value):
        """This function inserts a node at the front of the linked list

        Args:
            value (_type_): Node
        """ 
        # Create new node
        new_node = Node(value)

        # Check if linked list is empty, then make the new node the head of the linked list and also make the tail point to the new node
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then we point the new_node to the head of the list and point the previous of head to the new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_after(self, value, new_value):
        """This function inserts a node after a specified node

        Args:
            value (_type_): old value
            new_value (_type_): new value
        """
        # Start from head and search for value
        curr = self.head
        while curr:
            if curr.value == value:
                # If value is at the end of the list, self.tail, new_value becomes self.tail
                if curr == self.tail:
                    new_node = Node(new_value)
                    new_node.prev = self.tail
                    self.tail.next = new_node
                    self.tail = new_node
                # For any other location, we create a new node and reconnect the linked list
                else:
                    new_node = Node(new_value)
                    new_node.prev = curr
                    new_node.next = curr.next
                    curr.next = new_node
                    curr.next = new_node
                # return from this operation
                return
            curr = curr.next

    def remove_tail(self):
        """
        Remove the last node (i.e. the tail) of the linked list.
        """
        # If the list has only one item in it, then set head and tail 
        # to None resulting in an empty list.  This condition will also
        # cover an empty list.  Its okay to set to None again.
        if self.tail == self.head:
            self.tail = None
            self.head = None
            print("List is empty.")
        else:
            # If the list has more than one item in it, then only self.tail
            # will be affected.
            self.tail.prev.next = None
            self.tail = self.tail.prev
        return
    def __iter__(self):
        """Iterate throught the linked list
        """
        curr = self.head
        while curr:
            yield curr.value
            curr = curr.next

    def __str__(self):
        """Return a string representation of the linked list
        """
        output = "LinkedList["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output


# Sample test cases
print("\n=========== TESTS CASES ===========")
ll = LinkedList()
ll.remove_tail()     # List is empty.
ll.insert_at_head(2)
ll.insert_at_head(0)
ll.insert_at_head(8)
print(list(ll))   # [8, 0, 2]
ll.insert_after(0, 9)
ll.insert_after(8, 11)
print(ll)    # [8, 11, 0, 9, 2]
            



