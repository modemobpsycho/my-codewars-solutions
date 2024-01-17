def move_zeros(lst):
    return sorted(lst, key=lambda x: x == 0 and type(x) is not bool)
