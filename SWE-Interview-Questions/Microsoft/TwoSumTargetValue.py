# Brute forcing would give O(n^2)
def two_sum(num_list, target):
    # Make a hash map
    # value : index
    prevMap = {}

    for i, n in enumerate(num_list):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return
