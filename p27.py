import itertools
from euler_lib import miller_rabin
from multiprocessing import Pool
from operator import itemgetter


def max_primes(coeff):
    a, b = coeff

    def q(n):
        return n*n + a*n + b

    c = 0
    while miller_rabin(q(c)):
        c = c + 1
    return (a, b, c)


if __name__ == '__main__':
    p = Pool()
    a = range(-1000, 1000)
    b = range(-1000, 1000)

    coeffs = itertools.product(a, b)
    r = p.map(max_primes, coeffs)
    print max(r, key=itemgetter(2))
