#Mergesort


# base case: if list < 2, return
# split the list into two smaller lists
# for each smaller list, call Mergesort again
# merge the returned left and right sides by comparing the lowest unsorted index of each.
# return
import math

def mergesort(array):
    arraylen = len(array)
    if arraylen<2:
        return array
    mid = math.floor(arraylen/2)
    left = array[:mid]
    right = array[mid+1:]
    mergesort(left)
    mergesort(right)
    return merge(left, right, array)


def merge(left, right, array):
    '''merges the left and right arrays into a sorted array'''
    while left and right:
        if left[0] > right[0]:
            array.append(left.pop(0))
        else:
            array.append(right.pop(0))
    array+=left
    array+=right
    return array

if __name__ == '__main__':
    import pudb
    array = [2,5,6,9,1,33,4,9,345,6]
    pudb.set_trace()
    mergesort(array)