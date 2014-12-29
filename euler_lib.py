import random


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
    for i in range(s-1):
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
            for n in range(2*i, limit, i):
                a[n] = False


def num_to_list(n):
    """Convert integer to list of integers"""
    l = str(n)
    l = list(l)
    l = map(int, l)
    return list(l)


def list_to_num(l):
    """Convert list of integers to integer"""
    return sum(map(lambda x: x[0]*10**x[1], zip(l, reversed(range(0, len(l))))))


def pandigital(l):
    """Tests if list of integers is pandigital"""
    n = set(l)
    if all(map(lambda x: x in n, range(0, len(n)))):
        return list_to_num(l)


# http://stackoverflow.com/questions/4643647/fast-prime-factorization-module
def primesbelow(N):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    #""" Input N>=6, Returns a list of primes, 2 <= p < N """
    correction = N % 6 > 1
    N = {0:N, 1:N-1, 2:N+4, 3:N+3, 4:N+2, 5:N+1}[N%6]
    sieve = [True] * (N // 3)
    sieve[0] = False
    for i in range(int(N ** .5) // 3 + 1):
        if sieve[i]:
            k = (3 * i + 1) | 1
            sieve[k*k // 3::2*k] = [False] * ((N//6 - (k*k)//6 - 1)//k + 1)
            sieve[(k*k + 4*k - 2*k*(i%2)) // 3::2*k] = [False] * ((N // 6 - (k*k + 4*k 
- 2*k*(i%2))//6 - 1) // k + 1)
    return [2, 3] + [(3 * i + 1) | 1 for i in range(1, N//3 - correction) if sieve[i]]

smallprimeset = set(primesbelow(100000))
_smallprimeset = 100000


def isprime(n, precision=7):
    # http://en.wikipedia.org/wiki/Miller-Rabin_primality_test#Algorithm_and_running_time
    if n == 1 or n % 2 == 0:
        return False
    elif n < 1:
        raise ValueError("Out of bounds, first argument must be > 0")
    elif n < _smallprimeset:
        return n in smallprimeset

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for repeat in range(precision):
        a = random.randrange(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for r in range(s - 1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False

    return True


def pollard_brent(n):
    # https://comeoncodeon.wordpress.com/2010/09/18/pollard-rho-brent-integer-factorization/
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    y, c, m = random.randint(1, n-1), random.randint(1, n-1), random.randint(1, n-1)
    g, r, q = 1, 1, 1
    while g == 1:
        x = y
        for i in range(r):
            y = (pow(y, 2, n) + c) % n

        k = 0
        while k < r and g == 1:
            ys = y
            for i in range(min(m, r-k)):
                y = (pow(y, 2, n) + c) % n
                q = q * abs(x-y) % n
            g = gcd(q, n)
            k += m
        r *= 2
    if g == n:
        while True:
            ys = (pow(ys, 2, n) + c) % n
            g = gcd(abs(x - ys), n)
            if g > 1:
                break

    return g

smallprimes = primesbelow(1000)


# might seem low, but 1000*1000 = 1000000, so this will fully factor every
# composite < 1000000
def primefactors(n, sort=False):
    factors = []

    limit = int(n ** .5) + 1
    for checker in smallprimes:
        if checker > limit:
            break
        while n % checker == 0:
            factors.append(checker)
            n //= checker
            limit = int(n ** .5) + 1
            if checker > limit:
                break

    if n < 2:
        return factors

    while n > 1:
        if isprime(n):
            factors.append(n)
            break
        factor = pollard_brent(n)
        # trial division did not fully factor, switch to pollard-brent
        factors.extend(primefactors(factor))
        # recurse to factor the not necessarily prime factor returned by pollard-brent
        n //= factor

    if sort:
        factors.sort()

    return factors


def factorization(n):
    factors = {}
    for p1 in primefactors(n):
        try:
            factors[p1] += 1
        except KeyError:
            factors[p1] = 1
    return factors

totients = {}


def totient(n):
    if n == 0:
        return 1

    try:
        return totients[n]
    except KeyError:
        pass

    tot = 1
    for p, exp in factorization(n).items():
        tot *= (p - 1)  *  p ** (exp - 1)

    totients[n] = tot
    return tot


def gcd(a, b):
    if a == b:
        return a
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)
