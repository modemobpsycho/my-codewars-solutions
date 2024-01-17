def combos(n):
    results = []
    helper(n, [], 1, results)
    return results


def helper(target, combination, start, results):
    if target == 0:
        results.append(combination)
        return
    if target < 0:
        return

    for i in range(start, target + 1):
        helper(target - i, combination + [i], i, results)
