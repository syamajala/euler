import numpy as np


def main():
    g = np.loadtxt("p13.txt", dtype=np.float)
    g = map(int, g)
    g = str(sum(g))
    print(g[:10])

main()
