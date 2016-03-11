#Quicksort

#1. randomly choose a pivot
#2. compare to all other items and sort according to whther they are higher or lower than the pivot
#3. repeat on lower and igher groups until all items have been visited


import random

def quicksort(array):
  if len(array) < 2:
    return array
  else:
    pivotindex = random.choice(range(len(array)))
    pivot = array[pivotindex]
    less = []
    greater = []
    for i in range(len(array)):
        if i == pivotindex:
            continue
        if array[i] < pivot:
            less.append(array[i])
        else:
            greater.append(array[i])
    return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == '__main__':
    # import pudb
    # pudb.set_trace()
    print(quicksort([10, 5, 2, 3, 60, 50, 23, 10, 2]))