import math
from multiprocessing import Pool


def d(n):
    r = range(1, n//2+1)
    r = map(lambda x: x if not n % x else 0, r)
    return (n, sum(r))


def amicable(p):
    a, b = p
    if a == b:
        return
    elif d(b)[1] == a:
        return p

if __name__ == '__main__':
    p = Pool()
    n = range(1, 10001)
    r = p.map(d, n)
    a = p.map(amicable, r)
    a = [i for i in a if i]
    print a

    s = 0
    for i in a:
        s = s + i[0]
    print s
