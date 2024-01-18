def find_all(sum_dig, digs):
    numbers = [x for x in find_ascending(digs) if sum(x) == sum_dig]
    if not numbers:
        return []
    return [
        len(numbers),
        int("".join(map(str, numbers[0]))),
        int("".join(map(str, numbers[-1]))),
    ]


def find_ascending(d, start=1):
    if d == 1:
        for x in range(start, 10):
            yield [x]
    else:
        for x in range(start, 10):
            for y in find_ascending(d - 1, x):
                yield [x] + y
