def find_it(seq):
    return [item for item in set(seq) if seq.count(item) % 2][0]
