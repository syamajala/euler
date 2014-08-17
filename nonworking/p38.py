import euler_lib
import itertools


def nine_pandigital(n):
    return map(n.count, range(1, 10))


def good_product(n):
    return all(map(lambda x: True if (x == 1 or x == 0) else False, n))


def concatenate(ns):
    l = map(euler_lib.num_to_list, ns)
    return list(itertools.chain(*l))


def products(n):
    i = 1
    ps = [n]
    r = concatenate(ps)

    while True:
        if good_product(nine_pandigital(r)):
            i += 1
            ps.append(n*i)
            r = concatenate(ps)
        else:
            return ps


def main():
    pass
