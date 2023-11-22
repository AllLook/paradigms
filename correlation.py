from math import sqrt
from statistics import correlation


def correlat(arr_one, arr_two):
    return round(correlation(arr_one, arr_two), 4)


def correlat_double(x: list, y: list):
    average_x = sum(x) / len(x)
    average_y = sum(y) / len(y)
    list_x = [item - average_x for item in x]
    list_y = [item - average_y for item in y]
    numerator = sum((map(lambda item_1, item_2: item_1 * item_2, list_x, list_y)))
    list_x_double = sum(map(lambda item: item ** 2, list_x))
    list_y_double = sum(map(lambda item: item ** 2, list_y))
    denominator = sqrt(list_x_double * list_y_double)
    return round(numerator / denominator, 4)


if __name__ == '__main__':
    print(correlat([2, 4, 6, 8], [1, 3, 7, 13]))
    print(correlat_double([2, 4, 6, 8], [2, 4, 10, 12]))
