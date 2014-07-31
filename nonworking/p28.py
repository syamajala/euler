import numpy as np


def spiral(n):
    """Generates n x n spiral."""
    s = np.empty([n, n], dtype=int)
    start = n//2
    s[start, start] = 1

    idx = (start, start)
    entries = range(2, n*n)
    c = 0

    for k in range(1, n):
        i, j = idx
        for l in range(-k, k):
            pass

    return s
