from itertools import chain, combinations, permutations

first_list = ["abc"]

chained_list = list(chain("abc", ['d', 'e'], ('f', 'g')))

print(chained_list, end="\n")


# Get all combinations of length 2 from iterable "ABC"
print(list(combinations("ABC", 2)))

# Get all permutations of length 2 from ABC
print(list(permutations("ABC", 2)))
