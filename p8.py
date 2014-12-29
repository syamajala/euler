import itertools
import numpy as np


class grid():

    def __init__(self):
        self.g = np.loadtxt("p8.txt", np.int32)

    def left(self, i, j):
        if j < 13:
            return None
        r = 1
        for k in range(0, 13):
            r = r*self.g[i, j-k]
        return r

    def right(self, i, j):
        r = 1
        o = 0
        for k in range(0, 13):
            try:
                r = r*self.g[i, j+k]
            except IndexError:
                if i < 19:
                    r = r*self.g[i+1, o]
                    o = o + 1
                else:
                    return None
        return r

    def max_prod(self, c):
        return max(self.left(*c), self.right(*c))

    def solve(self):
        coords = itertools.product(range(0, 20), range(0, 50))
        s = map(lambda c: self.max_prod(c), coords)
        return max(s)


def main():
    g = grid()
    print(g.solve())

main()
