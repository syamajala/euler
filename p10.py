import euler_lib


def main():

    p = [i for i in euler_lib.primes(2000000)]
    print(sum(p))

main()
