class Node():
    def __init__(self, value = None):
        self.next = None
        self.value = value

class Stack():
    def __init__(self, value=None):
        self.head = Node(value)
        self.min = self.head.value

    def push(self, value=None):
        next_node = Node(value)
        next_node.next = self.head
        self.head = next_node

    def pop(self):
        result = self.head

        if self.head is None:
            return None
        self.head = self.head.next
        return result.value

    def peek(self):
        if self.head is None:
            return None
        return self.head.value

    # def min(self):

