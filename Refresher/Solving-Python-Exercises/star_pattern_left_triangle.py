def print_left_triangle():
    num_stars = 5
    i = 1
    while i <= num_stars:
        print(" " * (num_stars - i) + "*" * i)
        i += 1
