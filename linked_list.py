class Node:
    """Node for singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Singly linked list with basic insertion, deletion, and traversal."""
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def delete_at_index(self, index):
        if index < 0:
            raise IndexError("Index out of bounds")
        current = self.head
        prev = None
        i = 0
        while current:
            if i == index:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return current.data
            prev = current
            current = current.next
            i += 1
        raise IndexError("Index out of bounds")

    def traverse(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __str__(self):
        return '->'.join(str(data) for data in self.traverse())