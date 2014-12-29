import euler_lib
from itertools import compress, count, islice
from functools import partial
from operator import eq


def nth_item(n, item, iterable):
        # nth item taken from 
        # http://stackoverflow.com/questions/8337069/find-the-index-of-the-nth-item-in-a-list
        indicies = compress(count(), map(partial(eq, item), iterable))
        return next(islice(indicies, n, None), -1)


def main():
    n = range(3, 125000, 2)
    a = map(euler_lib.miller_rabin, n)
    n = list(n)
    n.insert(0, 2)
    a = list(a)
    a.insert(0, True)

    print(n[nth_item(10000, True, a)])

main()
