def process():
    with open("p18.txt", 'r') as f:
        return [map(int, i.split()) for i in f]


def traverse(triangle):
    r = triangle[0][0]
    idx = 0

    for i in triangle[1:]:
        if i[idx] > i[idx+1]:
            print(idx, i[idx])
            r = r + i[idx]
        else:
            print(idx+1, i[idx+1])
            r = r + i[idx+1]
            idx = idx+1

    return r


def main():
    triangle = process()
    r = traverse(triangle)
    print(r)

main()
