import itertools
from multiprocessing import Pool


def genc(ab, p):
    a, b = ab
    c = p-a-b
    if c < 0:
        return None
    elif a**2 + b**2 == c**2:
        return (a, b, c)


def lengths(p):
    ab = itertools.combinations(range(1, p+1), 2)
    coords = map(lambda x: genc(x, p), ab)
    coords = [x for x in coords if x is not None]
    return coords


if __name__ == '__main__':
    p = Pool()
    solns = p.map(lengths, range(1, 1001))
    r = map(len, solns)
    r = list(r)
    print(r.index(max(r))+1)
