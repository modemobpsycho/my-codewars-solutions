def min_value(digits):
    return int("".join([str(item) for item in sorted(set(digits))]))
