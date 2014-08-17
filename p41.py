import euler_lib


def main():
    p = euler_lib.primes(10000000)
    p = map(str, p)
    p = map(list, p)
    p = map(lambda x: map(int, x), p)
    p = map(euler_lib.pandigital, p)
    p = [i for i in p if i is not None]
    print p[-1]

main()
