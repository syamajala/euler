import itertools


def palindrome(n):
    l = list(str(n))
    rl = list(l)
    rl.reverse()
    if l == rl:
        return n


def main():
    nums = itertools.product(range(100, 1000), range(100, 1000))
    r = map(lambda x: x[0]*x[1], nums)
    r = map(palindrome, r)
    print max(r)

main()
