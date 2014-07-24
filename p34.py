import math


def equal_factorial(n):
    l = map(int, list(str(n)))
    l = map(math.factorial, l)
    if sum(l) == n:
        return n


def main():

    r = map(equal_factorial, range(3, 100000))
    r = [i for i in r if i is not None]
    print sum(r)
