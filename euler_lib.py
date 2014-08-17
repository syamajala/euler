def fibonacci():
    """Fibonacci numbers generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# taken from https://gist.github.com/sharnett/5479106
def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in xrange(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1


def miller_rabin(n):
    '''if n < 1,373,653, it is enough to test a = 2 and 3;
    if n < 9,080,191, it is enough to test a = 31 and 73;
    if n < 4,759,123,141, it is enough to test a = 2, 7, and 61;
    if n < 2,152,302,898,747, it is enough to test a = 2, 3, 5, 7, and 11;'''
    if n < 2:
        return False

    al = {}
    if n < 1373653:
        al = {2, 3}
    elif n < 9080191:
        al = {31, 73}
    elif n < 4759123141:
        al = {2, 7, 61}
    elif n < 2152302898747:
        al = {2, 3, 5, 7, 11}

    if n in al:
        return True

    d = n - 1
    s = 0

    while d % 2 == 0:
        d >>= 1
        s += 1

    for a in al:
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True


# http://stackoverflow.com/questions/3939660/sieve-of-eratosthenes-finding-primes-python
def primes(limit):
    """Sieve of Eratosthenes"""
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(2*i, limit, i):
                a[n] = False


def num_to_list(n):
    l = str(n)
    l = list(l)
    l = map(int, l)
    return l


def list_to_num(l):
    return sum(map(lambda x: x[0]*10**x[1], zip(l, reversed(range(0, len(l))))))


def pandigital(n):
    p = range(1, len(n)+1)
    if all(map(lambda x: x in n, p)):
        return list_to_num(n)
