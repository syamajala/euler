import itertools
import euler_lib
from multiprocessing import Pool


def circular(p):
    if all(map(euler_lib.miller_rabin, p)):
        return p


def rotate(p):
    n = len(p)
    r = [p]
    for i in range(1, n):
        p = p[-1:]+p[:n-1]
        r.append(p)
    return r


def main():
    p = euler_lib.primes(1000000)
    p = map(str, p)
    p = map(list, p)
    p = map(lambda x: map(int, x), p)
    p = map(rotate, p)
    p = map(lambda x: map(euler_lib.list_to_num, x), p)
    r = map(circular, p)
    r = [j for i in r if i is not None for j in i]
    r = set(r)
    print len(r)

main()
