import string


class namelist():

    def __init__(self):
        with open("p22.txt", 'r') as f:
            l = f.readline()
            names = l.split(',')
        names = map(lambda x: x.strip('"'), names)
        names.sort()
        self.names = names

    def name_value(self, n):
        v = map(lambda x: string.ascii_uppercase.index(x) + 1, list(n))
        return sum(v)*(self.names.index(n)+1)


def main():
    n = namelist()
    s = map(n.name_value, n.names)
    print(sum(s))

main()
