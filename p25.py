import euler_lib


def main():
    i = 0
    f = euler_lib.fibonacci()
    for x in f:
        if len(str(x)) == 1000:
            print(i)
            break
        i = i + 1

main()
