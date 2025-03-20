class Node: 
    def __init__(self, value): 
        self.value = value 
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        if self.head is not None:
            self.head.previous = new_node
        else:
            self.tail = new_node
        self.head = new_node
        
    def add_to_end(self, value):
        new_node = Node(value)
        new_node.prev = self.tail
        if self.tail is not None:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def remove_from_front(self, value):
        if not self.head:
            return None
        removed_value = self.head.value
        self.head = self.head.next
        if self.head is not None:
            self.head.previous = None
        else:
            self.tail = None
        return removed_value

    def remove_from_end(self, value):
        if not self.head:
            return None
        removed_value = self.tail.value
        self.tail = self.tail.prev
        if self.head is not None:
            self.head.previous = None
        else:
            self.tail = None
        return removed_value