from multiprocessing import Pool


def collatz(n):
    yield n
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n+1
        yield n


def seq_len(n):
    return sum(1 for _ in collatz(n))

if __name__ == '__main__':
    p = Pool()
    c = p.map(seq_len, range(1, 1000000))
    print(c.index(max(c))+1)
