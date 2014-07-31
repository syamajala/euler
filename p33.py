import itertools


def valid_cancellation(f):
    n, d = f
    new_f = None

    if n[1] == '0' and d[1] == '0':
        return None
    elif n[0] == d[0]:
        new_f = (float(n[1]), float(d[1]))
    elif n[1] == d[0]:
        new_f = (float(n[0]), float(d[1]))
    elif n[0] == d[1]:
        new_f = (float(n[1]), float(d[0]))
    elif n[1] == d[1]:
        new_f = (float(n[0]), float(d[0]))
    else:
        return None

    nn, nd = new_f
    if nn == 0 or nd == 0:
        return None

    n = float(n)
    d = float(d)

    if n/d == nn/nd and n/d < 1:
        return (n, d)


def main():
    nums = map(str, range(10, 101))
    fracs = itertools.product(nums, nums)
    r = map(valid_cancellation, fracs)
    r = [i for i in r if i]

    n = 1
    d = 1

    for i in r:
        n = n * i[0]
        d = d * i[1]

    print(n, d)

main()
