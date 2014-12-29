import itertools
import numpy as np


class grid():

    def __init__(self):
        self.g = np.loadtxt("p11.txt", np.int32)

    def up(self, i, j):
        if i > 16:
            return None
        return self.g[i, j]*self.g[i+1, j]*self.g[i+2, j]*self.g[i+3, j]

    def down(self, i, j):
        if i < 3:
            return None
        return self.g[i, j]*self.g[i-1, j]*self.g[i-2, j]*self.g[i-3, j]

    def left(self, i, j):
        if j < 3:
            return None
        return self.g[i, j]*self.g[i, j-1]*self.g[i, j-2]*self.g[i, j-3]

    def right(self, i, j):
        if j > 16:
            return None
        return self.g[i, j]*self.g[i, j+1]*self.g[i, j+2]*self.g[i, j+3]

    def left_diagonal(self, i, j):
        if i < 3 or j > 16:
            return None
        return self.g[i, j]*self.g[i-1, j+1]*self.g[i-2, j+2]*self.g[i-3, j+3]

    def right_diagonal(self, i, j):
        if i > 16 or j > 16:
            return None
        return self.g[i, j]*self.g[i+1, j+1]*self.g[i+2, j+2]*self.g[i+3, j+3]

    def max_prod(self, c):
        return max([self.up(*c), self.down(*c), self.left(*c), self.right(*c),
                    self.left_diagonal(*c), self.right_diagonal(*c)])

    def solve(self):
        coords = itertools.product(range(0, 20), range(0, 20))
        s = map(lambda c: self.max_prod(c), coords)
        return max(s)


def main():
    g = grid()
    print(g.solve())

main()
