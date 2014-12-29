def main():
    sum_of_squares = map(lambda x: x*x, range(1, 101))
    sum_of_squares = sum(sum_of_squares)

    square_of_sum = sum(range(1, 101))**2

    print(square_of_sum - sum_of_squares)

main()
