import euler_lib
from itertools import compress, count, imap, islice
from functools import partial
from operator import eq

# nth item taken from 
# http://stackoverflow.com/questions/8337069/find-the-index-of-the-nth-item-in-a-list
def nth_item(n, item, iterable):
        indicies = compress(count(), imap(partial(eq, item), iterable))
        return next(islice(indicies, n, None), -1)


def main():
    n = range(3, 125000, 2)
    a = map(euler_lib.miller_rabin, n)
    n.insert(0, 2)
    a.insert(0, True)

    print n[nth_item(10000, True, a)]

main()
