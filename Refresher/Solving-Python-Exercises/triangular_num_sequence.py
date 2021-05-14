# Given a range of the first 10 numbers,
# Iterate from start to end
# print sum of current and previous numbers


def print_triangular_number():
    for i in range(1, 11):
        running_sum = 0
        for j in range(1, i + 1):
            running_sum += j
        print(f"Iteration: {i} ====> summation: {running_sum}")
