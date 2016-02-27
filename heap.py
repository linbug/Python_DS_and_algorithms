#binary min heap

#Array implementation

# A complete binary tree can be implemented using an array
# The second element is the root
# considering the kth element:
    # The left child is the 2*kth index
    # The right child is the 2*k + 1 index
    # The parent is the floor(k/2) element
import math

class Heap:
    def __init__(self, root = None):
        self.data = [None, root]

    def percolate(self):
        current_index = len(self.data) -1
        parent_index = int(math.floor(current_index/2))
        current_value = self.data[current_index]
        parent_value = self.data[parent_index]
        while current_value < parent_value:
            self.data[parent_index] = current_value
            self.data[current_index] = parent_value
            current_index = parent_index
            parent_index = int(math.floor(current_index/2))
            current_value = self.data[current_index]
            parent_value = self.data[parent_index]

    def push(self, value):
        if not self.data[1]:
            self.data[1] = value
        else:
            self.data.append(value)
        self.percolate()

    # def pop(self):
