def product_fib(prod):
    if prod == 0:
        return [0, 1, True]
    a = 0
    b = 1
    while True:
        if b > a:
            a += b
        else:
            b += a
        if a * b == prod:
            return [a, b, True] if a < b else [b, a, True]
        elif a * b > prod:
            return [a, b, False] if a < b else [b, a, False]
