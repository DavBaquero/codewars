def comp(a, b):
    if a is None or b is None or len(a) != len(b):
        return False
    squared_a = [x * x for x in a]
    squared_a.sort()
    b.sort()
    return squared_a == b