def factorial():
    count = 1
    fact = 1
    while 1:
        yield fact
        count = count + 1
        fact = fact*count


def main():
    f = factorial()
    for i in range(1, 100):
        next(f)
    r = next(f)
    print(sum(map(int, list(str(r)))))

main()
