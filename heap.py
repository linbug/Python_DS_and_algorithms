#binary min heap

#Array implementation

# A complete binary tree can be implemented using an array
# The second element is the root
# considering the kth element:
    # The left child is the 2*kth index
    # The right child is the 2*k + 1 index
    # The parent is the floor(k/2) element
#delete_min function allows you to do heapsort
import math

class Heap:
    def __init__(self, root = None):
        self.data = [None, root]

    def percolate_up(self):
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

    def percolate_down(self):
        current_index = 1
        left_child_index = (current_index * 2 if len(self.data)-1 >= current_index * 2 else None)
        right_child_index = ((current_index * 2) + 1 if len(self.data)-1 >= (current_index * 2) + 1 else None)
        current_value = self.data[current_index]
        left_child_value = (self.data[left_child_index] if left_child_index else None)
        right_child_value = (self.data[right_child_index] if right_child_index else None)
        #if both children are smaller, swap with the smallest
        # if only one child is smaller, swap with the smaller
        while current_value > left_child_value or current_value > right_child_value:
            print('current value = ' + str(current_value))
            print('left child value = ' + str(left_child_value))
            print('right child value = ' + str(right_child_value))
            if current_value > left_child_value and current_value > right_child_value and right_child_value:
                if left_child_value <= right_child_value or (current_value > left_child_value and current_value < right_child_value):
                    if left_child_index<= len(self.data)-1 and left_child_index:
                        current_index, current_value, left_child_index, left_child_value, right_child_index, right_child_value\
                         = self.swap_child(current_index, current_value, left_child_index, left_child_value)
                        continue
                    else:
                        return
                else:
                    if right_child_index<= len(self.data)-1 and right_child_index:
                        current_index, current_value, left_child_index, left_child_value, right_child_index, right_child_value\
                         = self.swap_child(current_index, current_value, right_child_index, right_child_value)
                        continue
                    else:
                        return
            elif current_value > left_child_value:
                if left_child_index<= len(self.data)-1 and left_child_index:
                    current_index, current_value, left_child_index, left_child_value, right_child_index, right_child_value\
                     = self.swap_child(current_index, current_value, left_child_index, left_child_value)
                    continue
                else:
                    return
            else:
                if right_child_index<= len(self.data)-1 and right_child_index:
                    current_index, current_value, left_child_index, left_child_value, right_child_index, right_child_value\
                     = self.swap_child(current_index, current_value, right_child_index, right_child_value)
                    continue
                else:
                    return

    def swap_child(self, current_index, current_value, direction_index, direction_value):
        self.data[current_index] = direction_value
        self.data[direction_index] = current_value
        print('swapping ' + str(current_value) + ' with ' + str(direction_value))
        current_index = direction_index
        current_value = self.data[current_index]
        left_child_index = current_index * 2
        right_child_index = left_child_index + 1
        left_child_value = (self.data[left_child_index] if len(self.data)-1>=left_child_index else None)
        right_child_value = (self.data[left_child_index] if len(self.data)-1>=right_child_index else None)
        return current_index, current_value, left_child_index, left_child_value, right_child_index, right_child_value

    def insert(self, value):
        if not self.data[1]:
            self.data[1] = value
        else:
            self.data.append(value)
        self.percolate_up()

    def delete_min(self):
        min = self.data[1]
        self.data[1] = self.data.pop(len(self.data)-1) if len(self.data)-1 >= 2 else None
        if self.data[1]:
            self.percolate_down()
        return min

if __name__ == '__main__':
    heap = Heap()
    heap.insert(5)
    heap.insert(4)
    heap.insert(12)
    heap.insert(2)
    heap.insert(70)
    heap.insert(90)
