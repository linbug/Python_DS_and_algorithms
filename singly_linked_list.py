class Singly_linked_list:
    def __init__(self, head):
        self.head = Node(head)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def add_next(self, next):
        self.next = Node(next)