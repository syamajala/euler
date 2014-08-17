def cycle(n):
    pass


def main():
    f = map(lambda x: 1.0/x, range(1, 1001))
    f = map(lambda x: str(x)[2:], f)
    f = map(list, f)
    f = map(lambda x: map(int, x), f)

main()
