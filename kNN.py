# k nearest neighbours

# Strategy: in order to determine what category an item falls into, we compare its position in an n-dimensional space to previously classified items

import math

classes = {1:'A',2:'A',2:'A',4:'B',5:'B',6:'B'}

preferences = {1:[1,1],2:[2,2],3:[1,2],4:[5,2],5:[5,3],6:[7,3]}

def calculate_distance(item1,item2):
    total = 0
    for i in range(len(preferences[item1])):
        to_square = preferences[item1][i] - preferences[item2][i]
        to_square = to_square**2
        total+=to_square
    return math.sqrt(total)

if __name__ == '__main__':
    import pudb
    pudb.set_trace()
    calculate_distance(1,2)