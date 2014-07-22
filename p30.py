def main():
    r = []
    for i in range(1000, 1000000):
        if sum_of_fifths(map(int, str(i))) == i:
            r.append(i)

    print r
    print sum(r)


def sum_of_fifths(l):
    return sum(map(lambda x: pow(x, 5), l))

main()
