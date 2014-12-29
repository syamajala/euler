import num2words


def count(n):
    l = list(n)
    l = [i for i in l if (i != '-' and i != ' ')]
    return len(l)


def main():

    n = range(1, 1001)
    n = map(num2words.num2words, n)
    c = map(count, n)
    print(sum(c))

main()
