import euler_lib


def rotate(l):
    p = list(l)
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
    p = map(lambda x: list(map(euler_lib.list_to_num, x)), p)
    r = filter(lambda x: all(map(euler_lib.miller_rabin, x)), p)
    r = list(r)
    print(len(r))

main()
