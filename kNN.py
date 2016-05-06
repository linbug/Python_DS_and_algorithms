# k nearest neighbours

# Strategy: in order to determine what category an item falls into, we compare its position in an n-dimensional space to previously classified items

# we don't want to have to recalculate each of the distances each time for the same training set.
# So I should separate out calculation of distances from classification

import math

classes = ['A','A','A','B','B','B'] #e.g. A = cat B = dog

data = [[1,1],[2,2],[1,2],[5,2],[5,3],[7,3]] #training data (feature vectors). Could be length and width of each animal

def calculate_distance(item1,item2):
    total = 0
    for i in range(len(item1)):
        to_square = item1[i] - item2[i]
        to_square = to_square**2
        total+=to_square
    return math.sqrt(total)

def calculate_nearest_neighbours(k, point, data, classes):
    distances = []
    for item in data:
        distances.append(calculate_distance(point,item))
    return distances


if __name__ == '__main__':
    import pudb
    pudb.set_trace()
    calculate_nearest_neighbours(3,[5,5],data,classes)