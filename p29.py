import itertools


def main():

    p = itertools.product(range(2, 101), range(2, 101))
    p = map(lambda x: pow(*x), p)
    p = set(p)
    print(len(p))

main()
