def fibonacci():
    """Fibonacci numbers generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def main():

    r = 0
    f = fibonacci()
    for x in f:
        if x%2 == 0:
            if x < 4000000:
                r = r + x
            else:
                break

    print(r)

main()
