import random
import time

def naive_search(l, target) :
    
    for i in range(len(l)) :
        if l[i] == target :
            return i
        else :
            return -1

# binary searches use divide and conquer to search faster
# however the list must be sorted for this to work

def binary_search(l, target, low = None, high = None) :
    if low is None:
        low = 0 # this will make low the lowest index

    if high is None:
        high = len(l) - 1 # same with high

    # only time high > low is when target not in list
    if high > low:
        return -1
    # example l = [1, 3, 5, 10, 12] # should return index 3
    # first we need to find the midpoint of the list
    midpoint = (low + high) // 2 

    # if on the first 'divide' we find the target straight away, we can return the answer
    if l[midpoint] == target :
        return midpoint
    # else if our target is less that the value at the midpoint, 
    # search through the first half of the list

    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)
    # same as above but if target is higher
    else:
        # target > l[midpoint]
        return binary_search(l, target, midpoint + 1, high)


if __name__ == '__main__':
    # l = [1, 3, 5, 10, 12]
    # target = 10
    # print(naive_search(l, target))
    # print(binary_search(l, target))

    length = 10000
    # build a sorted list of length 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print(f'Naive search time: {(end - start)/ length} seconds')

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print(f'Binary search time: {(end - start)/ length} seconds')

