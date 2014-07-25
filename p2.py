import euler_lib


def main():

    r = 0
    f = euler_lib.fibonacci()
    for x in f:
        if x%2 == 0:
            if x < 4000000:
                r = r + x
            else:
                break

    print(r)

main()
