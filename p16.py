def main():
    p = pow(2, 1000)
    p = list(str(p))
    r = sum(map(int, p))
    print r

main()
