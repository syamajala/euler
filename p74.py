from multiprocessing import Pool
import math
import euler_lib


def chain(n):
    r = []
    s = n
    l = euler_lib.num_to_list(s)

    while len(r) < 60 and s not in r:
        r.append(s)
        l = map(math.factorial, l)
        s = sum(l)
        l = euler_lib.num_to_list(s)

    return r


if __name__ == '__main__':
    l = range(1, 1000001)
    with Pool() as pool:
        l = pool.map(chain, l)

        l = filter(lambda x: len(x) == 60, l)
        l = list(l)
        print(len(l))
