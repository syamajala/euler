import euler_lib
from multiprocessing import Pool


def lefttoright(n):

    s = [n[i:] for i in range(0, len(n))]
    ns = map(euler_lib.list_to_num, s)
    p = map(euler_lib.miller_rabin, ns)
    return all(p)


def righttoleft(n):

    s = [n[:i] for i in reversed(range(1, len(n)+1))]
    ns = map(euler_lib.list_to_num, s)
    p = map(euler_lib.miller_rabin, ns)
    return all(p)


def truncatable(p):

    if len(p) == 1:
        return None

    if lefttoright(p) and righttoleft(p):
        return euler_lib.list_to_num(p)


if __name__ == '__main__':

    pl = Pool()
    p = euler_lib.primes(1000000)
    p = pl.map(str, p)
    p = pl.map(list, p)
    p = map(lambda x: map(int, x), p)
    r = pl.map(truncatable, p)
    r = [i for i in r if i is not None]
    print(sum(r))
