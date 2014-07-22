def main():
    s = sum(map(lambda i: pow(i, i), range(1, 1001)))
    s = list(str(s))
    r = map(int, s[-10:])
    print r

main()
