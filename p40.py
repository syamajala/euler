def main():

    l = range(1, 1000001)
    l = map(str, l)
    s = ''.join(l)
    l = [s[1-1], s[10-1], s[100-1], s[1000-1], s[10000-1], s[100000-1], s[1000000-1]]
    l = map(int, l)
    r = reduce(lambda x, y: x*y, l)
    print r

main()
