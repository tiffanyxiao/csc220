
def sum_to_n(n, size, limit=None):
    """Produce all lists of `size` positive integers in decreasing order
    that add up to `n`. from stack overflow"""
    if size == 1:
        yield [n]
        return
    if limit is None:
        limit = n
    start = (n + size - 1) // size
    stop = min(limit, n - size + 1) + 1
    for i in range(start, stop):
        for tail in sum_to_n(n - i, size - 1, i):
            yield [i] + tail


def main():
    superlist = []
    for i in range(1,100):
        for partition in sum_to_n(100, i):
            print(partition)


main()
