def main():
    with open('p42.txt') as f:
        l = f.readlines()
    l = l[0]
    l = l.split(',')
    l = map(lambda x: x.strip('"'), l)
    l = [map(lambda x: ord(x) - 64, i) for i in l]
    l = map(sum, l)
    t = map(lambda x: 0.5*x*(x+1), range(1, 21))
    t = list(t)
    r = map(lambda x: x in t, l)
    r = filter(None, r)
    r = list(r)
    print(len(r))

main()
