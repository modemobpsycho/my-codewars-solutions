def max_sequence(arr):
    if arr == []:
        return 0
    curMax = arr[0]
    glMax = arr[0]
    for i in range(1, len(arr)):
        curMax = max(arr[i], arr[i] + curMax)
        if curMax > glMax:
            glMax = curMax
    return glMax if glMax > 0 else 0
